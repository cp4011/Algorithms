from numpy import *


def load_dataset(filename):
    length = len(open(filename).readline().split('\t'))
    data_matrix = []
    label_matrix = []
    fr = open(filename)
    for line in fr.readlines():
        line_array = line.strip().split('\t')
        cur_line = []
        for i in range(length - 1):
            cur_line.append(float(line_array[i]))
        data_matrix.append(cur_line)
        label_matrix.append(float(line_array[-1]))
    return data_matrix, label_matrix


def stand_regeres(x_array, y_array):
    x_matrix = mat(x_array)
    y_matrix = mat(y_array).T
    xTx = x_matrix.T * x_matrix
    if linalg.det(xTx) == 0.0:                # 矩阵行列式|A|=0,则矩阵不可逆
        print("This matrix is singular, cannot do inverse")
        return
    ws = xTx.I * x_matrix.T * y_matrix
    return ws                               # 回归系数向量
# 测试
# x_arr, y_arr = load_dataset('ex0.txt')            # 输入的x0默认为1
# print(stand_regeres(x_arr, y_arr))


# 局部加权线性回归 LWLR
def lwlr(testPoint, xArr, yArr, k=1.0):
    xMat = mat(xArr)
    yMat = mat(yArr).T
    m = shape(xMat)[0]
    weights = mat(eye((m)))                                   # 创建对角矩阵（权重矩阵是个方阵，阶数=样本点个数)
    for j in range(m):
        diffMat = testPoint - xMat[j, :]                      # 计算样本点与预测值的距离
        weights[j, j] = exp(diffMat*diffMat.T/(-2.0 * k**2))  # 计算高斯核函数的权重矩阵W：权重值大小随着样本点与待遇测点距离的递增，以指数级衰减
    xTx = xMat.T * (weights * xMat)
    if linalg.det(xTx) == 0.0:                                # 判断是否可逆
        print("This matrix is singular, cannot do inverse")
        return
    ws = xTx.I * (xMat.T * (weights * yMat))
    return testPoint * ws


def lwlrTest(testArr, xArr, yArr, k=1.0):              # loops over all the data points and applies lwlr to each one
    m = shape(testArr)[0]
    yHat = zeros(m)
    for i in range(m):
        yHat[i] = lwlr(testArr[i], xArr, yArr, k)
    return yHat


def lwlrTestPlot(xArr, yArr, k=1.0):
    import matplotlib.pyplot as plt
    yHat = zeros(shape(yArr))
    xCopy = mat(xArr)
    xCopy.sort(0)
    for i in range(shape(xArr)[0]):
        yHat[i] = lwlr(xCopy[i], xArr, yArr, k)
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.plot([i[1] for i in xArr], yArr, 'ro')
    ax.plot(xCopy, yHat)
    plt.show()
# test
# xArr, yArr = load_dataset('ex0.txt')
# print(lwlr(xArr[0], xArr, yArr, 1.0))
# lwlrTestPlot(xArr, yArr)


def rssError(yArr, yHatArr):        # 计算预测误差（参数为 数组）
    return((yArr-yHatArr)**2).sum()

# test
# abX, abY = load_dataset('abalone.txt')
# yHat01 = lwlrTest(abX[0:99], abX[0:99], abY[0:99], k=0.1)
# yHat1 = lwlrTest(abX[0:99], abX[0:99], abY[0:99], k=1)
# yHat10 = lwlrTest(abX[0:99], abX[0:99], abY[0:99], k=10)
# print(rssError(abY[0:99], yHat01.T))
# print(rssError(abY[0:99], yHat1.T))
# print(rssError(abY[0:99], yHat10.T))


# 缩减系数之“岭”回归
def ridgeRegres(xMat, yMat, lam=0.2):
    xTx = xMat.T*xMat
    denom = xTx+eye(shape(xMat)[1])*lam
    if linalg.det(denom) == 0.0:
        print("This matrix is singular,cannot do inverse")
        return
    ws = denom.I*(xMat.T*yMat)
    return ws


def ridgeTest(xArr, yArr):
    xMat = mat(xArr)
    yMat = mat(yArr).T        # 数据标准化（特征标准化处理），减去均值，除以方差
    yMean = mean(yMat, 0)
    yMat = yMat-yMean
    xMeans = mean(xMat, 0)
    xVar = var(xMat, 0)
    xMat = (xMat-xMeans)/xVar
    numTestPts = 30
    wMat = zeros((numTestPts, shape(xMat)[1]))
    for i in range(numTestPts):
        ws = ridgeRegres(xMat, yMat, exp(i-10))
        wMat[i, :] = ws.T
    return wMat
# test
# xArr, yArr = load_dataset('abalone.txt')
# ridgrWeights = ridgeTest(xArr, yArr)
# print(ridgrWeights)
# import matplotlib.pyplot as plt
# ax = plt.figure()
# ax = ax.add_subplot(111)
# ax.plot(ridgrWeights)
# plt.show()


def regularize(xMat):           # regularize by columns（下个函数要调用）
    inMat = xMat.copy()
    inMeans = mean(inMat, 0)    # calc mean then subtract it off
    inVar = var(inMat, 0)       # calc variance of Xi then divide by it
    inMat = (inMat - inMeans)/inVar
    return inMat


# 前向逐步线性回归
def stageWise(xArr, yArr, eps=0.01, numIt=100):
    xMat = mat(xArr)
    yMat = mat(yArr).T
    yMean = mean(yMat, 0)
    yMat = yMat-yMean           # can also regularize ys but will get smaller coef
    xMat = regularize(xMat)
    m, n = shape(xMat)
    # returnMat = zeros((numIt,n)) # testing code remove
    returnMat = zeros((numIt, n))
    ws = zeros((n, 1))
    wsTest = ws.copy()
    wsMax = ws.copy()
    for i in range(numIt):
        print(ws.T)
        lowestError = inf
        for j in range(n):
            for sign in [-1, 1]:                     # 两次循环，计算增加或者减少该特征对误差的影响
                wsTest = ws.copy()
                wsTest[j] += eps*sign
                yTest = xMat*wsTest
                rssE = rssError(yMat.A, yTest.A)     # 平方误差
                if rssE < lowestError:
                    lowestError = rssE
                    wsMax = wsTest
        ws = wsMax.copy()
        returnMat[i, :] = ws.T
    return returnMat

# test
# xArr, yArr = load_dataset('abalone.txt')
# print(stageWise(xArr, yArr, 0.01, 200))