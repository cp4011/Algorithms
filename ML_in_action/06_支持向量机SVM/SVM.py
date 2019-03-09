from numpy import *
import matplotlib.pyplot as plt

"""SMO算法工作原理：每次循环中选择两个alpha进行优化处理。一旦找到一对合适的alpha，那么就增大其中一个同时减小另一个。
这里所谓的“合适”就是指两个alpha必须要符合一定的条件，条件之一就是这两个alpha必须要在间隔边界之外，另一个条件则是这两个
alpha还没有进行过区间化处理或者不在边界上
"""


# SMO算法相关辅助中的辅助函数
# 1.解析文本数据函数，提取每个样本的特征组成向量，添加到数据矩阵; 添加样本标签到标签向量
def loadDataSet(filename):
    data_matrix = []
    label_matrix = []
    with open(filename, 'r') as fr:
        for line in fr.readlines():
            line_array = line.strip().split('\t')       # strip删除头尾空白字符（空格+回车），再进行分割
            data_matrix.append([float(line_array[0]), float(line_array[1])])    # 填充数据集
            label_matrix.append(float(line_array[2]))                           # 填充类别标签
    return data_matrix, label_matrix                    # 返回数据集和标签列表
# 测试
# data_matrix, label_matrix = loadDataSet("testSet.txt")
# print(label_matrix)


# 2.在样本集中采取随机选择的方法选取第二个不等于第一个alphai的优化向量alphaj
def selectJrand(i, m):
    """
    Function：   随机选择

    Input：      i：alpha下标
                m：alpha数目

    Output： j：随机选择的alpha下标
    """
    # 初始化下标j
    j = i
    # 随机化产生j，直到不等于i
    while (j == i):
        j = int(random.uniform(0,m))
    # 返回j的值
    return j


def clipAlpha(aj, H, L):
    """
    Function：   设定alpha阈值

    Input：      aj：alpha的值
                H：alpha的最大值
                L：alpha的最小值

    Output： aj：处理后的alpha的值
    """
    # 如果输入alpha的值大于最大值，则令aj=H
    if aj > H:
        aj = H
    # 如果输入alpha的值小于最小值，则令aj=L
    if L > aj:
        aj = L
    # 返回处理后的alpha的值
    return aj


"""简化版SMO伪代码：
创建一个alpha向量并将其初始化为0向量
当迭代次数小于最大迭代次数时（外循环）：
    对数据集中的每个数据向量（内循环）：
        如果该数据向量可以被优化：
            随机选择另外一个数据向量
            同时优化这两个向量
            如果两个向量都不能被优化，退出内循环
    如果所有向量都没被优化，则增加迭代数目，继续下一次循环
"""


def smoSimple(dataMatIn, classLabels, C, toler, maxIter):
    """
    Function：   简化版SMO算法

    Input：      dataMatIn：数据集
                classLabels：类别标签
                C：常数C
                toler：容错率
                maxIter：最大的循环次数

    Output： b：常数项
                alphas：数据向量
    """
    # 将输入的数据集和类别标签转换为NumPy矩阵
    dataMatrix = mat(dataMatIn); labelMat = mat(classLabels).transpose()
    # 初始化常数项b，初始化行列数m、n
    b = 0; m,n = shape(dataMatrix)
    # 初始化alphas数据向量为0向量
    alphas = mat(zeros((m,1)))
    # 初始化iter变量，存储的是在没有任何alpha改变的情况下遍历数据集的次数
    iter = 0
    # 外循环，当迭代次数小于maxIter时执行
    while (iter < maxIter):
        # alpha改变标志位每次都要初始化为0
        alphaPairsChanged = 0
        # 内循环，遍历所有数据集
        for i in range(m):
            # multiply将alphas和labelMat进行矩阵相乘，求出法向量w(m,1),w`(1,m)
            # dataMatrix * dataMatrix[i,:].T，求出输入向量x(m,1)
            # 整个对应输出公式f(x)=w`x + b
            fXi = float(multiply(alphas, labelMat).T * (dataMatrix * dataMatrix[i,:].T)) + b
            # 计算误差
            Ei = fXi - float(labelMat[i])
            # 如果标签与误差相乘之后在容错范围之外，且超过各自对应的常数值，则进行优化
            if ((labelMat[i]*Ei < -toler) and (alphas[i] < C)) or ((labelMat[i] * Ei > toler) and (alphas[i] > 0)):
                # 随机化选择另一个数据向量
                j = selectJrand(i, m)
                # 对此向量进行同样的计算
                fXj = float(multiply(alphas, labelMat).T * (dataMatrix * dataMatrix[j,:].T)) + b
                # 计算误差
                Ej = fXj - float(labelMat[j])
                # 利用copy存储刚才的计算值，便于后期比较
                alphaIold = alphas[i].copy(); alpahJold = alphas[j].copy()
                # 保证alpha在0和C之间
                if (labelMat[i] != labelMat[j]):
                    L = max(0, alphas[j] - alphas[i])
                    H = min(C, C + alphas[j] - alphas[i])
                else:
                    L = max(0, alphas[j] + alphas[i] - C)
                    H = min(C, alphas[j] + alphas[i])
                # 如果界限值相同，则不做处理直接跳出本次循环
                if L == H: print("L == H"); continue
                # 最优修改量，求两个向量的内积（核函数）
                eta = 2.0 * dataMatrix[i,:] * dataMatrix[j,:].T - dataMatrix[i,:] * dataMatrix[i,:].T - dataMatrix[j,:] * dataMatrix[j,:].T
                # 如果最优修改量大于0，则不做处理直接跳出本次循环，这里对真实SMO做了简化处理
                if eta >= 0: print("eta >= 0"); continue
                # 计算新的alphas[j]的值
                alphas[j] -= labelMat[j] * (Ei - Ej) / eta
                # 对新的alphas[j]进行阈值处理
                alphas[j] = clipAlpha(alphas[j], H, L)
                # 如果新旧值差很小，则不做处理跳出本次循环
                if (abs(alphas[j] - alpahJold) < 0.00001): print("j not moving enough"); continue
                # 对i进行修改，修改量相同，但是方向相反
                alphas[i] += labelMat[j] * labelMat[i] * (alpahJold - alphas[j])
                # 新的常数项
                b1 = b - Ei - labelMat[i] * (alphas[i] - alphaIold) * dataMatrix[i,:] * dataMatrix[i,:].T - labelMat[i] * (alphas[j] - alpahJold) * dataMatrix[i,:] * dataMatrix[j,:].T
                b2 = b - Ej - labelMat[i] * (alphas[i] - alphaIold) * dataMatrix[i,:] * dataMatrix[j,:].T - labelMat[j] * (alphas[j] - alpahJold) * dataMatrix[j,:] * dataMatrix[j,:].T
                # 谁在0到C之间，就听谁的，否则就取平均值
                if (0 < alphas[i]) and (C > alphas[i]): b = b1
                elif (0 < alphas[j]) and (C > alphas[j]): b = b2
                else: b = (b1 + b2) / 2.0
                # 标志位加1
                alphaPairsChanged += 1
                # 输出迭代次数，alphas的标号以及标志位的值
                print("iter: %d i: %d, pairs changed %d" % (iter, i, alphaPairsChanged))
        # 如果标志位没变，即没有进行优化，那么迭代值加1
        if (alphaPairsChanged == 0): iter += 1
        # 否则迭代值为0
        else: iter = 0
        # 打印迭代次数
        print("iteration number: %d" % iter)
    # 返回常数项和alphas的数据向量
    return b, alphas


"""和简化版一样，完整版也需要一些支持函数。
首要的事情就是建立一个数据结构来保存所有的重要值，而这个过程可以通过一个对象来完成；
对于给定的alpha值，第一个辅助函数calcEk()能够计算E值并返回（因为调用频繁，所以必须要单独拎出来）；
selectJ()用于选择第二个alpha或者说内循环的alpha值，选择合适的值以保证在每次优化中采用最大步长；
updateEk()用于计算误差值并将其存入缓存中。
"""


# SMO完整版(Non-Kernel VErsions below)
class optStruct:
    """
    Function：   存放运算中重要的值
    Input：      dataMatIn：数据集
                classLabels：类别标签
                C：常数C
                toler：容错率
    Output： X：数据集
                labelMat：类别标签
                C：常数C
                tol：容错率
                m：数据集行数
                b：常数项
                alphas：alphas矩阵
                eCache：误差缓存
    """
    def __init__(self, dataMatIn, classLabels, C, toler):
        self.X = dataMatIn
        self.labelMat = classLabels
        self.C = C
        self.tol = toler
        self.m = shape(dataMatIn)[0]
        self.alphas = mat(zeros((self.m, 1)))
        self.b = 0
        self.eCache = mat(zeros((self.m, 2)))


def calcEk(oS, k):
    """
    Function：   计算误差值E
    Input：      oS：数据结构
                k：下标
    Output： Ek：计算的E值
    """
    # 计算fXk，整个对应输出公式f(x)=w`x + b
    fXk = float(multiply(oS.alphas, oS.labelMat).T * (oS.X * oS.X[k,:].T)) + oS.b
    # 计算E值
    Ek = fXk - float(oS.labelMat[k])
    # 返回计算的误差值E
    return Ek


def selectJ(i, oS, Ei):
    """
    Function：   选择第二个alpha的值

    Input：      i：第一个alpha的下标
                oS：数据结构
                Ei：计算出的第一个alpha的误差值

    Output： j：第二个alpha的下标
                Ej：计算出的第二个alpha的误差值
    """
    # 初始化参数值
    maxK = -1; maxDeltaE = 0; Ej = 0
    # 构建误差缓存
    oS.eCache[i] = [1, Ei]
    # 构建一个非零列表，返回值是第一个非零E所对应的alpha值，而不是E本身
    validEcacheList = nonzero(oS.eCache[:, 0].A)[0]
    # 如果列表长度大于1，说明不是第一次循环
    if (len(validEcacheList)) > 1:
        # 遍历列表中所有元素
        for k in validEcacheList:
            # 如果是第一个alpha的下标，就跳出本次循环
            if k == i: continue
            # 计算k下标对应的误差值
            Ek = calcEk(oS, k)
            # 取两个alpha误差值的差值的绝对值
            deltaE = abs(Ei - Ek)
            # 最大值更新
            if (deltaE > maxDeltaE):
                maxK = k; maxDeltaE = deltaE; Ej = Ek
        # 返回最大差值的下标maxK和误差值Ej
        return maxK, Ej
    # 如果是第一次循环，则随机选择alpha，然后计算误差
    else:
        j = selectJrand(i, oS.m)
        Ej = calcEk(oS, j)
    # 返回下标j和其对应的误差Ej
    return j, Ej


def updateEk(oS, k):
    """
    Function：   更新误差缓存
    Input：      oS：数据结构
                j：alpha的下标
    Output： 无
    """
    # 计算下表为k的参数的误差
    Ek = calcEk(oS, k)
    # 将误差放入缓存
    oS.eCache[k] = [1, Ek]


"""优化例程
  接下来简单介绍一下用于寻找决策边界的优化例程。大部分代码和之前的smoSimple()是一样的，区别在于：
使用了自己的数据结构，该结构在oS中传递；
使用selectJ()而不是selectJrand()来选择第二个alpha的值；
在alpha值改变时更新Ecache。
"""


def innerL(i, oS):
    """
    Function：   完整SMO算法中的优化例程
    Input：      oS：数据结构
                i：alpha的下标
    Output： 无
    """
    # 计算误差
    Ei = calcEk(oS, i)
    # 如果标签与误差相乘之后在容错范围之外，且超过各自对应的常数值，则进行优化
    if ((oS.labelMat[i]*Ei < -oS.tol) and (oS.alphas[i] < oS.C)) or ((oS.labelMat[i]*Ei > oS.tol) and (oS.alphas[i] > 0)):
        # 启发式选择第二个alpha值
        j, Ej = selectJ(i, oS, Ei)
        # 利用copy存储刚才的计算值，便于后期比较
        alphaIold = oS.alphas[i].copy(); alpahJold = oS.alphas[j].copy();
        # 保证alpha在0和C之间
        if (oS.labelMat[i] != oS.labelMat[j]):
            L = max(0, oS.alphas[j] - oS. alphas[i])
            H = min(oS.C, oS.C + oS.alphas[j] - oS.alphas[i])
        else:
            L = max(0, oS.alphas[j] + oS.alphas[i] - oS.C)
            H = min(oS.C, oS.alphas[j] + oS.alphas[i])
        # 如果界限值相同，则不做处理直接跳出本次循环
        if L == H: print("L==H"); return 0
        # 最优修改量，求两个向量的内积（核函数）
        eta = 2.0 * oS.X[i, :]*oS.X[j, :].T - oS.X[i, :]*oS.X[i, :].T - oS.X[j, :]*oS.X[j, :].T
        # 如果最优修改量大于0，则不做处理直接跳出本次循环，这里对真实SMO做了简化处理
        if eta >= 0: print("eta>=0"); return 0
        # 计算新的alphas[j]的值
        oS.alphas[j] -= oS.labelMat[j]*(Ei - Ej)/eta
        # 对新的alphas[j]进行阈值处理
        oS.alphas[j] = clipAlpha(oS.alphas[j], H, L)
        # 更新误差缓存
        updateEk(oS, j)
        # 如果新旧值差很小，则不做处理跳出本次循环
        if (abs(oS.alphas[j] - alpahJold) < 0.00001): print("j not moving enough"); return 0
        # 对i进行修改，修改量相同，但是方向相反
        oS.alphas[i] += oS.labelMat[j] * oS.labelMat[i] * (alpahJold - oS.alphas[j])
        # 更新误差缓存
        updateEk(oS, i)
        # 更新常数项
        b1 = oS.b - Ei - oS.labelMat[i] * (oS.alphas[i] - alphaIold) * oS.X[i, :]*oS.X[i, :].T - oS.labelMat[j] * (oS.alphas[j] - alpahJold) * oS.X[i, :]*oS.X[j, :].T
        b2 = oS.b - Ej - oS.labelMat[i] * (oS.alphas[i] - alphaIold) * oS.X[i, :]*oS.X[j, :].T - oS.labelMat[j] * (oS.alphas[j] - alpahJold) * oS.X[j, :]*oS.X[j, :].T
        # 谁在0到C之间，就听谁的，否则就取平均值
        if (0 < oS.alphas[i]) and (oS.C > oS.alphas[i]): oS.b = b1
        elif (0 < oS.alphas[j]) and (oS.C > oS.alphas[i]): oS.b = b2
        else: oS.b = (b1 + b2) / 2.0
        # 成功返回1
        return 1
    # 失败返回0
    else: return 0


"""外循环代码
  外循环代码的输入和函数smoSimple()完全一样。整个代码的主体是while循环，终止条件：当迭代次数超过指定的最大值，或者遍历
整个集合都未对任意alpha对进行修改时，就退出循环。while循环内部与smoSimple()中有所不同，一开始的for循环在数据集上遍历任意
可能的alpha。通过innerL()来选择第二个alpha，并在可能时对其进行优化处理。如果有任意一对alpha值发生改变，就会返回1.第二个
for循环遍历所有的非边界alpha值，也就是不在边界0或C上的值。
"""


def smoP(dataMatIn, classLabels, C, toler, maxIter):
    """
    Function：   完整SMO算法
    Input：      dataMatIn：数据集
                classLabels：类别标签
                C：常数C
                toler：容错率
                maxIter：最大的循环次数
    Output： b：常数项
                alphas：数据向量
    """
    # 新建数据结构对象
    oS = optStruct(mat(dataMatIn), mat(classLabels).transpose(), C, toler)
    # 初始化迭代次数
    iter = 0
    # 初始化标志位
    entireSet = True; alphaPairsChanged = 0
    # 终止条件：迭代次数超限、遍历整个集合都未对alpha进行修改
    while (iter < maxIter) and ((alphaPairsChanged > 0) or (entireSet)):
        alphaPairsChanged = 0
        # 根据标志位选择不同的遍历方式
        if entireSet:
            # 遍历任意可能的alpha值
            for i in range(oS.m):
                # 选择第二个alpha值，并在可能时对其进行优化处理
                alphaPairsChanged += innerL(i, oS)
                print("fullSet, iter: %d i: %d, pairs changed %d" % (iter, i, alphaPairsChanged))
            # 迭代次数累加
            iter += 1
        else:
            # 得出所有的非边界alpha值
            nonBoundIs = nonzero((oS.alphas.A > 0) * (oS.alphas.A < C))[0]
            # 遍历所有的非边界alpha值
            for i in nonBoundIs:
                # 选择第二个alpha值，并在可能时对其进行优化处理
                alphaPairsChanged += innerL(i, oS)
                print("non-bound, iter: %d i: %d, pairs changed %d" % (iter, i, alphaPairsChanged))
            # 迭代次数累加
            iter += 1
        # 在非边界循环和完整遍历之间进行切换
        if entireSet: entireSet = False
        elif (alphaPairsChanged == 0): entireSet =True
        print("iteration number: %d" % iter)
    # 返回常数项和数据向量
    return oS.b, oS.alphas


"""分类测试
可以拿我们计算出来的alpha值进行分类了。首先必须基于alpha值得到超平面，这也包括了w的计算
"""


def calcWs(alphas, dataArr, classLabels):
    """
    Function：   计算W
    Input：      alphas：数据向量
                dataArr：数据集
                classLabels：类别标签
    Output： w：w*x+b中的w
    """
    # 初始化参数
    X = mat(dataArr); labelMat = mat(classLabels).transpose()
    # 获取数据行列值
    m, n = shape(X)
    # 初始化w
    w = zeros((n, 1))
    # 遍历alpha，更新w
    for i in range(m):
        w += multiply(alphas[i]*labelMat[i],X[i,:].T)
    # 返回w值
    return w


# 测试test
# dataArr, labelArr = loadDataSet('testSet.txt')
# b, alphas = smoP(dataArr, labelArr, 0.6, 0.001, 40)
# ws = calcWs(alphas, dataArr, labelArr)
# # print(ws)
# datMat = mat(dataArr)
# print(datMat[0] * mat(ws)+b, labelArr[0])
# print(datMat[1] * mat(ws)+b, labelArr[1])
# print(datMat[2] * mat(ws)+b, labelArr[2])


"""至此，线性分类器介绍完了，如果数据集非线性可分，那么我们就需要引入核函数的概念了"""


# 核函数实现
"""如果在svmMLiA.py文件中添加一个函数并稍作修改，那么我们就能在已有代码中使用核函数了（所有与核函数实现相关的函数，函数
名末尾都是K）。其中主要区分代码在innerLK()和calcEk()中
"""
# 新添加的核转换函数，主要用于填充结构体和后续的计算
def kernelTrans(X, A, kTup):
    """
    Function：   核转换函数
    Input：      X：数据集
                A：某一行数据
                kTup：核函数信息
    Output： K：计算出的核向量
    """
    # 获取数据集行列数
    m, n = shape(X)
    # 初始化列向量
    K = mat(zeros((m, 1)))
    # 根据键值选择相应核函数
    # lin表示的是线性核函数
    if kTup[0] == 'lin': K = X * A.T
    # rbf表示径向基核函数
    elif kTup[0] == 'rbf':
        for j in range(m):
            deltaRow = X[j, :] - A
            K[j] = deltaRow * deltaRow.T
        # 对矩阵元素展开计算，而不像在MATLAB中一样计算矩阵的逆
        K =  exp(K/(-1*kTup[1]**2))
    # 如果无法识别，就报错
    else: raise NameError('Houston We Have a Problem -- That Kernel is not recognized')
    # 返回计算出的核向量
    return K


# 其他函数
class optStructK:
    """
    Function：   存放运算中重要的值

    Input：      dataMatIn：数据集
                classLabels：类别标签
                C：常数C
                toler：容错率
                kTup：速度参数

    Output： X：数据集
                labelMat：类别标签
                C：常数C
                tol：容错率
                m：数据集行数
                b：常数项
                alphas：alphas矩阵
                eCache：误差缓存
                K：核函数矩阵
    """
    def __init__(self, dataMatIn, classLabels, C, toler, kTup):
        self.X = dataMatIn
        self.labelMat = classLabels
        self.C = C
        self.tol = toler
        self.m = shape(dataMatIn)[0]
        self.alphas = mat(zeros((self.m, 1)))
        self.b = 0
        self.eCache = mat(zeros((self.m, 2)))

        """ 主要区分 """
        self.K = mat(zeros((self.m, self.m)))
        for i in range(self.m):
            self.K[:,i] = kernelTrans(self.X, self.X[i,:], kTup)
        """ 主要区分 """

def calcEkK(oS, k):
    """
    Function：   计算误差值E
    Input：      oS：数据结构
                k：下标
    Output： Ek：计算的E值
    """
    """ 主要区分 """
    # 计算fXk，整个对应输出公式f(x)=w`x + b
    # fXk = float(multiply(oS.alphas, oS.labelMat).T * (oS.X * oS.X[k,:].T)) + oS.b
    fXk = float(multiply(oS.alphas, oS.labelMat).T*oS.K[:, k] + oS.b)
    """ 主要区分 """

    # 计算E值
    Ek = fXk - float(oS.labelMat[k])
    # 返回计算的误差值E
    return Ek

def selectJK(i, oS, Ei):
    """
    Function：   选择第二个alpha的值
    Input：      i：第一个alpha的下标
                oS：数据结构
                Ei：计算出的第一个alpha的误差值
    Output： j：第二个alpha的下标
                Ej：计算出的第二个alpha的误差值
    """
    # 初始化参数值
    maxK = -1; maxDeltaE = 0; Ej = 0
    # 构建误差缓存
    oS.eCache[i] = [1, Ei]
    # 构建一个非零列表，返回值是第一个非零E所对应的alpha值，而不是E本身
    validEcacheList = nonzero(oS.eCache[:, 0].A)[0]
    # 如果列表长度大于1，说明不是第一次循环
    if (len(validEcacheList)) > 1:
        # 遍历列表中所有元素
        for k in validEcacheList:
            # 如果是第一个alpha的下标，就跳出本次循环
            if k == i: continue
            # 计算k下标对应的误差值
            Ek = calcEkK(oS, k)
            # 取两个alpha误差值的差值的绝对值
            deltaE = abs(Ei - Ek)
            # 最大值更新
            if (deltaE > maxDeltaE):
                maxK = k; maxDeltaE = deltaE; Ej = Ek
        # 返回最大差值的下标maxK和误差值Ej
        return maxK, Ej
    # 如果是第一次循环，则随机选择alpha，然后计算误差
    else:
        j = selectJrand(i, oS.m)
        Ej = calcEkK(oS, j)
    # 返回下标j和其对应的误差Ej
    return j, Ej

def updateEkK(oS, k):
    """
    Function：   更新误差缓存
    Input：      oS：数据结构
                j：alpha的下标
    Output： 无
    """
    #计算下表为k的参数的误差
    Ek = calcEkK(oS, k)
    #将误差放入缓存
    oS.eCache[k] = [1, Ek]


def innerLK(i, oS):
    """
    Function：   完整SMO算法中的优化例程
    Input：      oS：数据结构
                i：alpha的下标
    Output： 无
    """
    # 计算误差
    Ei = calcEkK(oS, i)
    # 如果标签与误差相乘之后在容错范围之外，且超过各自对应的常数值，则进行优化
    if ((oS.labelMat[i]*Ei < -oS.tol) and (oS.alphas[i] < oS.C)) or ((oS.labelMat[i]*Ei > oS.tol) and (oS.alphas[i] > 0)):
        # 启发式选择第二个alpha值
        j, Ej = selectJK(i, oS, Ei)
        # 利用copy存储刚才的计算值，便于后期比较
        alphaIold = oS.alphas[i].copy(); alpahJold = oS.alphas[j].copy();
        # 保证alpha在0和C之间
        if (oS.labelMat[i] != oS.labelMat[j]):
            L = max(0, oS.alphas[j] - oS. alphas[i])
            H = min(oS.C, oS.C + oS.alphas[j] - oS.alphas[i])
        else:
            L = max(0, oS.alphas[j] + oS.alphas[i] - oS.C)
            H = min(oS.C, oS.alphas[j] + oS.alphas[i])
        # 如果界限值相同，则不做处理直接跳出本次循环
        if L == H: print("L==H"); return 0

        """ 主要区分 """
        # 最优修改量，求两个向量的内积（核函数）
        # eta = 2.0 * oS.X[i, :]*oS.X[j, :].T - oS.X[i, :]*oS.X[i, :].T - oS.X[j, :]*oS.X[j, :].T
        eta = 2.0 * oS.K[i, j] - oS.K[i, i] - oS.K[j, j]
        """ 主要区分 """

        # 如果最优修改量大于0，则不做处理直接跳出本次循环，这里对真实SMO做了简化处理
        if eta >= 0: print("eta>=0"); return 0
        # 计算新的alphas[j]的值
        oS.alphas[j] -= oS.labelMat[j]*(Ei - Ej)/eta
        # 对新的alphas[j]进行阈值处理
        oS.alphas[j] = clipAlpha(oS.alphas[j], H, L)
        # 更新误差缓存
        updateEkK(oS, j)
        # 如果新旧值差很小，则不做处理跳出本次循环
        if (abs(oS.alphas[j] - alpahJold) < 0.00001): print("j not moving enough"); return 0
        # 对i进行修改，修改量相同，但是方向相反
        oS.alphas[i] += oS.labelMat[j] * oS.labelMat[i] * (alpahJold - oS.alphas[j])
        # 更新误差缓存
        updateEkK(oS, i)

        """ 主要区分 """
        # 更新常数项
        # b1 = oS.b - Ei - oS.labelMat[i] * (oS.alphas[i] - alphaIold) * oS.X[i, :]*oS.X[i, :].T - oS.labelMat[j] * (oS.alphas[j] - alpahJold) * oS.X[i, :]*oS.X[j, :].T
        # b2 = oS.b - Ej - oS.labelMat[i] * (oS.alphas[i] - alphaIold) * oS.X[i, :]*oS.X[j, :].T - oS.labelMat[j] * (oS.alphas[j] - alpahJold) * oS.X[j, :]*oS.X[j, :].T
        b1 = oS.b - Ei - oS.labelMat[i] * (oS.alphas[i] - alphaIold) * oS.K[i, i] - oS.labelMat[j] * (oS.alphas[j] - alpahJold) * oS.K[i, j]
        b2 = oS.b - Ej - oS.labelMat[i] * (oS.alphas[i] - alphaIold) * oS.K[i, j] - oS.labelMat[j] * (oS.alphas[j] - alpahJold) * oS.K[j, j]
        """ 主要区分 """

        # 谁在0到C之间，就听谁的，否则就取平均值
        if (0 < oS.alphas[i]) and (oS.C > oS.alphas[i]): oS.b = b1
        elif (0 < oS.alphas[j]) and (oS.C > oS.alphas[i]): oS.b = b2
        else: oS.b = (b1 + b2) / 2.0
        # 成功返回1
        return 1
    # 失败返回0
    else: return 0


def smoPK(dataMatIn, classLabels, C, toler, maxIter, kTup = ('lin', 0)):
    """
    Function：   完整SMO算法
    Input：      dataMatIn：数据集
                classLabels：类别标签
                C：常数C
                toler：容错率
                maxIter：最大的循环次数
                kTup：速度参数
    Output： b：常数项
                alphas：数据向量
    """
    # 新建数据结构对象
    oS = optStructK(mat(dataMatIn), mat(classLabels).transpose(), C, toler, kTup)
    # 初始化迭代次数
    iter = 0
    # 初始化标志位
    entireSet = True; alphaPairsChanged = 0
    # 终止条件：迭代次数超限、遍历整个集合都未对alpha进行修改
    while (iter < maxIter) and ((alphaPairsChanged > 0) or (entireSet)):
        alphaPairsChanged = 0
        # 根据标志位选择不同的遍历方式
        if entireSet:
            # 遍历任意可能的alpha值
            for i in range(oS.m):
                # 选择第二个alpha值，并在可能时对其进行优化处理
                alphaPairsChanged += innerLK(i, oS)
                print("fullSet, iter: %d i: %d, pairs changed %d" % (iter, i, alphaPairsChanged))
            # 迭代次数累加
            iter += 1
        else:
            # 得出所有的非边界alpha值
            nonBoundIs = nonzero((oS.alphas.A > 0) * (oS.alphas.A < C))[0]
            # 遍历所有的非边界alpha值
            for i in nonBoundIs:
                # 选择第二个alpha值，并在可能时对其进行优化处理
                alphaPairsChanged += innerLK(i, oS)
                print("non-bound, iter: %d i: %d, pairs changed %d" % (iter, i, alphaPairsChanged))
            # 迭代次数累加
            iter += 1
        # 在非边界循环和完整遍历之间进行切换
        if entireSet: entireSet = False
        elif (alphaPairsChanged == 0): entireSet =True
        print("iteration number: %d" % iter)
    # 返回常数项和数据向量
    return oS.b, oS.alphas


"""测试函数。整个代码中最重要的是for循环开始的那两行，他们给出了如何利用核函数进行分类。首先利用结构初始化方法中使用过的
kernelTrans()函数，得到转换后的数据。然后，再用其与前面的alpha及类别标签值求积。特别需要注意观察的是，我们是如何做到只需
要支持向量数据就可以进行分类的
"""


def testRbf(k1=1.3):
    """
    Function：   利用核函数进行分类的径向基测试函数
    Input：      k1：径向基函数的速度参数
    Output： 输出打印信息
    """
    # 导入数据集
    dataArr, labelArr = loadDataSet('testSetRBF.txt')
    # 调用Platt SMO算法
    b, alphas = smoPK(dataArr, labelArr, 200, 0.00001, 10000, ('rbf', k1))
    # 初始化数据矩阵和标签向量
    datMat = mat(dataArr); labelMat = mat(labelArr).transpose()
    # 记录支持向量序号
    svInd = nonzero(alphas.A > 0)[0]
    # 读取支持向量
    sVs = datMat[svInd]
    # 读取支持向量对应标签
    labelSV = labelMat[svInd]
    # 输出打印信息
    print("there are %d Support Vectors" % shape(sVs)[0])
    # 获取数据集行列值
    m, n = shape(datMat)
    # 初始化误差计数
    errorCount = 0
    # 遍历每一行，利用核函数对训练集进行分类
    for i in range(m):
        # 利用核函数转换数据
        kernelEval = kernelTrans(sVs, datMat[i,:], ('rbf', k1))
        # 仅用支持向量预测分类
        predict = kernelEval.T * multiply(labelSV, alphas[svInd]) + b
        # 预测分类结果与标签不符则错误计数加一
        if sign(predict) != sign(labelArr[i]): errorCount += 1
    # 打印输出分类错误率
    print("the training error rate is: %f" % (float(errorCount)/m))
    #导入测试数据集
    dataArr, labelArr = loadDataSet('testSetRBF2.txt')
    # 初始化误差计数
    errorCount = 0
    #初始化数据矩阵和标签向量
    datMat = mat(dataArr); labelMat = mat(labelArr).transpose()
    # 获取数据集行列值
    m, n = shape(datMat)
    # 遍历每一行，利用核函数对测试集进行分类
    for i in range(m):
        #利用核函数转换数据
        kernelEval = kernelTrans(sVs, datMat[i,:], ('rbf', k1))
        # 仅用支持向量预测分类
        predict = kernelEval.T * multiply(labelSV, alphas[svInd]) + b
        # 预测分类结果与标签不符则错误计数加一
        if sign(predict) != sign(labelArr[i]): errorCount += 1
    # 打印输出分类错误率
    print("the test error rate is: %f" % (float(errorCount)/m))
# test
# testRbf()


# SVM识别手写数据集
def img2vector(filename):
    """
    Function：   32*32图像转换为1*1024向量
    Input：      filename：文件名称字符串
    Output： returnVect：转换之后的1*1024向量
    """
    # 初始化要返回的1*1024向量
    returnVect = zeros((1, 1024))
    # 打开文件
    fr = open(filename)
    # 读取文件信息
    for i in range(32):
        # 循环读取文件的前32行
        lineStr = fr.readline()
        for j in range(32):
            # 将每行的头32个字符存储到要返回的向量中
            returnVect[0, 32*i+j] = int(lineStr[j])
    # 返回要输出的1*1024向量
    return returnVect


def loadImages(dirName):
    """
    Function：   加载图片
    Input：      dirName：文件路径
    Output： trainingMat：训练数据集
                hwLabels：数据标签
    """
    from os import listdir
    # 初始化数据标签
    hwLabels = []
    # 读取文件列表
    trainingFileList = listdir(dirName)
    # 读取文件个数
    m = len(trainingFileList)
    # 初始化训练数据集
    trainingMat = zeros((m, 1024))
    # 填充数据集
    for i in range(m):
        # 遍历所有文件
        fileNameStr = trainingFileList[i]
        # 提取文件名称
        fileStr = fileNameStr.split('.')[0]
        # 提取数字标识
        classNumStr = int(fileStr.split('_')[0])
        # 数字9记为-1类
        if classNumStr == 9: hwLabels.append(-1)
        # 其他数字记为+1类
        else: hwLabels.append(1)
        # 提取图像向量，填充数据集
        trainingMat[i, :] = img2vector('%s/%s' % (dirName, fileNameStr))
    # 返回数据集和数据标签
    return trainingMat, hwLabels


def testDigits(kTup = ('rbf', 10)):
    """
    Function：   手写数字分类函数
    Input：      kTup：核函数采用径向基函数
    Output： 输出打印信息
    """
    # 导入数据集
    dataArr, labelArr = loadImages('trainingDigits')
    # 调用Platt SMO算法
    b, alphas = smoPK(dataArr, labelArr, 200, 0.0001, 10000, kTup)
    # 初始化数据矩阵和标签向量
    datMat = mat(dataArr); labelMat = mat(labelArr).transpose()
    # 记录支持向量序号
    svInd = nonzero(alphas.A > 0)[0]
    # 读取支持向量
    sVs = datMat[svInd]
    # 读取支持向量对应标签
    labelSV = labelMat[svInd]
    # 输出打印信息
    print("there are %d Support Vectors" % shape(sVs)[0])
    # 获取数据集行列值
    m, n = shape(datMat)
    # 初始化误差计数
    errorCount = 0
    # 遍历每一行，利用核函数对训练集进行分类
    for i in range(m):
        # 利用核函数转换数据
        kernelEval = kernelTrans(sVs, datMat[i, :], kTup)
        # 仅用支持向量预测分类
        predict = kernelEval.T * multiply(labelSV, alphas[svInd]) + b
        # 预测分类结果与标签不符则错误计数加一
        if sign(predict) != sign(labelArr[i]): errorCount += 1
    # 打印输出分类错误率
    print("the training error rate is: %f" % (float(errorCount)/m))
    # 导入测试数据集
    dataArr, labelArr = loadImages('testDigits')
    # 初始化误差计数
    errorCount = 0
    # 初始化数据矩阵和标签向量
    datMat = mat(dataArr); labelMat = mat(labelArr).transpose()
    # 获取数据集行列值
    m, n = shape(datMat)
    # 遍历每一行，利用核函数对测试集进行分类
    for i in range(m):
        # 利用核函数转换数据
        kernelEval = kernelTrans(sVs, datMat[i, :], kTup)
        # 仅用支持向量预测分类
        predict = kernelEval.T * multiply(labelSV, alphas[svInd]) + b
        # 预测分类结果与标签不符则错误计数加一
        if sign(predict) != sign(labelArr[i]): errorCount += 1
    # 打印输出分类错误率
    print("the test error rate is: %f" % (float(errorCount)/m))

testDigits(('rbf', 20))

"""支持向量机是一种分类器。之所以称为“机”是因为它会产生一个二值决策结果，即它是一种决策“机”。支持向量机的泛化错误率
较低，具有良好的学习能力，且学到的结果具有很好的推广性。这些优点使得支持向量机十分流行，有些人认为他是监督学习中
最好的定式算法
"""