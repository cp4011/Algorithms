from numpy import *
def loadSimpData():
    datMat = matrix([[1. , 2.1],
                    [2. ,  1.1],
                    [1.3,  1. ],
                    [1. ,  1. ],
                    [2. ,  1. ]])
    classLabels = [1.0, 1.0, -1.0, -1.0, 1.0]
    return datMat, classLabels


'''构建单层决策树
将最小错误率minEroor设为无穷大
对数据集中的每一个特征（第一层循环）：
    对每个步长（第二层循环）：
        对每个不等号（第三层循环）：
            建立一颗单层决策树并利用加权数据集对它进行测试
            如果错误率低于minError，则将当前单层决策树设为最佳单层决策树
返回最佳单层决策树
'''


def stumpClassify(dataMatrix, dimen, threshVal, threshIneq):
    """
    Function：   通过阈值比较对数据进行分类

    Input：      dataMatrix：数据集
                dimen：数据集列数
                threshVal：阈值
                threshIneq：比较方式：lt，gt

    Output： retArray：分类结果
    """
    # 新建一个列向量用于存放分类结果，初始化都为1
    retArray = ones((shape(dataMatrix)[0], 1))
    # lt：小于，gt；大于；根据阈值进行分类，并将分类结果存储到retArray
    if threshIneq == 'lt':
        retArray[dataMatrix[:, dimen] <= threshVal] = -1.0
    else:
        retArray[dataMatrix[:, dimen] > threshVal] = -1.0       # 所有不满足不等式要求的元素都设置为 -1
    # 返回分类结果
    return retArray


def buildStump(dataArr, classLabels, D):
    """
    Function：   找到最低错误率的单层决策树

    Input：      dataArr：数据集
                classLabels：数据标签
                D：权重向量（样本集中每个样本点具有一个权重）

    Output： bestStump：分类结果
            minError：最小错误率
            bestClasEst：最佳单层决策树
    """
    # 初始化数据集和数据标签
    dataMatrix = mat(dataArr); labelMat = mat(classLabels).T
    # 获取行列值
    m, n = shape(dataMatrix)
    # 初始化步数，用于在特征的所有可能值上进行遍历
    numSteps = 10.0
    # 初始化字典，用于存储给定权重向量D时所得到的最佳单层决策树的相关信息
    bestStump = {}
    # 初始化类别估计值
    bestClasEst = mat(zeros((m, 1)))
    # 将最小错误率设无穷大，之后用于寻找可能的最小错误率
    minError = inf
    # 遍历数据集中每一个特征
    for i in range(n):
        # 获取数据集的最大最小值
        rangeMin = dataMatrix[:, i].min(); rangeMax = dataMatrix[:, i].max()
        # 根据步数求得步长
        stepSize = (rangeMax - rangeMin) / numSteps
        # 遍历每个步长
        for j in range(-1, int(numSteps) + 1):
            # 遍历每个不等号
            for inequal in ['lt', 'gt']:
                # 设定阈值
                threshVal = (rangeMin + float(j) * stepSize)
                # 通过阈值比较对数据进行分类
                predictedVals = stumpClassify(dataMatrix, i, threshVal, inequal)
                # 初始化错误计数向量
                errArr = mat(ones((m, 1)))
                # 如果预测结果和标签相同，则相应位置0
                errArr[predictedVals == labelMat] = 0
                # 计算权值误差，这就是AdaBoost和分类器交互的地方
                weightedError = D.T * errArr
                # 打印输出所有的值
                # print("split: dim %d, thresh %.2f, thresh ineqal: %s, the weighted error is %.3f" % (i, threshVal, inequal, weightedError))
                # 如果错误率低于minError，则将当前单层决策树设为最佳单层决策树，更新各项值
                if weightedError < minError:
                    minError = weightedError
                    bestClasEst = predictedVals.copy()
                    bestStump['dim'] = i
                    bestStump['thresh'] = threshVal
                    bestStump['ineq'] = inequal
    # 返回最佳单层决策树，最小错误率，类别估计值
    return bestStump, minError, bestClasEst


'''AdaBoost算法伪代码：
对每次迭代：
    利用buildStump()函数找到最佳的单层决策树
    将最佳单层决策树加入到单层决策树数组
    计算alpha
    计算新的权重向量D
    更新累计类别估计值
    如果错误率等于0.0，则退出循环
'''


def adaBoostTrainDS(dataArr, classLabels, numIt = 40):
    """
    Function：   找到最低错误率的单层决策树

    Input：      dataArr：数据集
                classLabels：数据标签
                numIt：迭代次数

    Output： weakClassArr：单层决策树列表
            aggClassEst：类别估计值
    """
    # 初始化列表，用来存放单层决策树的信息
    weakClassArr = []
    # 获取数据集行数
    m = shape(dataArr)[0]
    # 初始化向量D每个值均为1/m，D包含每个数据点的权重
    D = mat(ones((m, 1))/m)
    # 初始化列向量，记录每个数据点的类别估计累计值
    aggClassEst = mat(zeros((m, 1)))
    # 开始迭代
    for i in range(numIt):
        # 利用buildStump()函数找到最佳的单层决策树
        bestStump, error, classEst = buildStump(dataArr, classLabels, D)
        # print("D: ", D.T)
        # 根据公式计算alpha的值，max(error, 1e-16)用来确保在没有错误时不会发生除零溢出
        alpha = float(0.5 * log((1.0 - error) / max(error, 1e-16)))     # alpha定义为 0.5*ln[(1-错误率）/错误率]
        # 保存alpha的值
        bestStump['alpha'] = alpha
        # 填入数据到列表
        weakClassArr.append(bestStump)
        # print("classEst: ", classEst.T)
        # 为下一次迭代计算D（根据公式）
        expon = multiply(-1 * alpha * mat(classLabels).T, classEst)
        D = multiply(D, exp(expon))
        D = D / D.sum()
        # 累加类别估计值
        aggClassEst += alpha * classEst
        # print("aggClassEst: ", aggClassEst.T)
        # 计算错误率，aggClassEst本身是浮点数，需要通过sign来得到二分类结果
        aggErrors = multiply(sign(aggClassEst) != mat(classLabels).T, ones((m, 1)))
        errorRate = aggErrors.sum() / m
        print("total error: ", errorRate)
        # 如果总错误率为0则跳出循环
        if errorRate == 0.0:
            break
    # 返回单层决策树列表和累计错误率
    return weakClassArr
    # return weakClassArr, aggClassEst


def adaClassify(datToClass, classifierArr):
    """
    Function：   AdaBoost分类函数

    Input：      datToClass：待分类样例
                classifierArr：多个弱分类器组成的数组

    Output： sign(aggClassEst)：分类结果
    """
    # 初始化数据集
    dataMatrix = mat(datToClass)
    # 获得待分类样例个数
    m = shape(dataMatrix)[0]
    # 构建一个初始化为0的列向量，记录每个数据点的类别估计累计值
    aggClassEst = mat(zeros((m, 1)))
    # 遍历每个弱分类器
    for i in range(len(classifierArr)):
        # 基于stumpClassify得到类别估计值
        classEst = stumpClassify(dataMatrix, classifierArr[i]['dim'], classifierArr[i]['thresh'], classifierArr[i]['ineq'])
        # 累加类别估计值
        aggClassEst += classifierArr[i]['alpha'] * classEst
        # 打印aggClassEst，以便我们了解其变化情况
        # print(aggClassEst)
    # 返回分类结果，aggClassEst大于0则返回+1，否则返回-1
    return sign(aggClassEst)
# test
# dataArr, labelArr = loadSimpData()
# classiferArr = adaBoostTrainDS(dataArr, labelArr, 30)
# print(adaClassify([0, 0], classiferArr))
# print(adaClassify([[5, 5], [0, 0]], classiferArr))


def loadDataSet(fileName):
    """
    Function：   自适应数据加载函数

    Input：      fileName：文件名称

    Output： dataMat：数据集
                labelMat：类别标签
    """
    # 自动获取特征个数，这是和之前不一样的地方
    numFeat = len(open(fileName).readline().split('\t'))
    # 初始化数据集和标签列表
    dataMat = []; labelMat = []
    # 打开文件
    fr = open(fileName)
    # 遍历每一行
    for line in fr.readlines():
        # 初始化列表，用来存储每一行的数据
        lineArr = []
        # 切分文本
        curLine = line.strip().split('\t')
        # 遍历每一个特征，某人最后一列为标签
        for i in range(numFeat-1):
            # 将切分的文本全部加入行列表中
            lineArr.append(float(curLine[i]))
        # 将每个行列表加入到数据集中
        dataMat.append(lineArr)
        # 将每个标签加入标签列表中
        labelMat.append(float(curLine[-1]))
    # 返回数据集和标签列表
    return dataMat, labelMat


# test
dataArr, labelArr = loadDataSet('horseColicTraining2.txt')
classiferArr = adaBoostTrainDS(dataArr, labelArr, 10)
# 测试已经训练好的分类器，即数组classiferArr ：多个弱分类器组成的数组
testArr, testLabelArr = loadDataSet('horseColicTest2.txt')
prediction10 = adaClassify(testArr, classiferArr)
errArr = mat(ones((67, 1)))
err_num = errArr[prediction10 != mat(testLabelArr).T].sum()
print("error rate is %f" % (err_num / 67))

