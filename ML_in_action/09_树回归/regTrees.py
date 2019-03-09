"""创建回归树
binSplitDataSet通过数组过滤切分数据集，createTree递归建立树，输入参数决定树的类型，leafType给出建立叶节点的函数，因此
该参数也决定了要建立的是模型树还是回归树，errType代表误差计算函数，ops是一个包含树构建所需的其他参数的元组
"""
from numpy import *
# 载入数据


def loadDataSet(fileName):
    dataMat = []
    fr = open(fileName)
    for line in fr.readlines():
        curLine = line.strip().split('\t')
        fltLine = list(map(float, curLine))         # 将每行映射成浮点数，python3返回值改变，所以需要list()
        dataMat.append(fltLine)
    return dataMat


# 切分数据集为两个子集
def binSplitDataSet(dataSet, feature, value):       # 数据集 待切分特征 特征值
    mat0 = dataSet[nonzero(dataSet[:, feature] > value)[0], :]
    mat1 = dataSet[nonzero(dataSet[:, feature] <= value)[0], :]
    # 下面原书代码报错 index 0 is out of bounds,使用上面两行代码
    # mat0 = dataSet[nonzero(dataSet[:, feature] > value)[0], :][0]
    # mat1 = dataSet[nonzero(dataSet[:, feature] <= value)[0], :][0]
    return mat0, mat1


# Tree结点类型：回归树
def regLeaf(dataSet):                               # 生成叶结点，在回归树中是目标变量特征的均值
    return mean(dataSet[:, -1])


# 误差计算函数：回归误差
def regErr(dataSet):            # 计算目标的平方误差（均方误差*总样本数）
    return var(dataSet[:, -1]) * shape(dataSet)[0]


# 二元切分
def chooseBestSplit(dataSet, leafType=regLeaf, errType=regErr, ops=(1, 4)):
    # 切分特征的参数阈值，用户初始设置好
    tolS = ops[0]               # 允许的误差下降值
    tolN = ops[1]               # 切分的最小样本数
    # 若所有特征值都相同，停止切分
    if len(set(dataSet[:, -1].T.tolist()[0])) == 1:     # 倒数第一列转化成list 不重复
        return None, leafType(dataSet)                  # 如果剩余特征数为1，停止切分1。
        # 找不到好的切分特征，调用regLeaf直接生成叶结点
    m,n = shape(dataSet)
    S = errType(dataSet)                                # 最好的特征通过计算平均误差
    bestS = inf; bestIndex = 0; bestValue = 0
    for featIndex in range(n-1):                        # 遍历数据的每个属性特征
        # for splitVal in set(dataSet[:,featIndex]): python3报错修改为下面
        for splitVal in set((dataSet[:, featIndex].T.tolist())[0]):         # 遍历每个特征里不同的特征值
            mat0, mat1 = binSplitDataSet(dataSet, featIndex, splitVal)      # 对每个特征进行二元分类
            if (shape(mat0)[0] < tolN) or (shape(mat1)[0] < tolN): continue
            newS = errType(mat0) + errType(mat1)
            if newS < bestS:                                                # 更新为误差最小的特征
                bestIndex = featIndex
                bestValue = splitVal
                bestS = newS
    # 如果切分后误差效果下降不大，则取消切分，直接创建叶结点
    if (S - bestS) < tolS:
        return None, leafType(dataSet)                                       # 停止切分2
    mat0, mat1 = binSplitDataSet(dataSet, bestIndex, bestValue)
    # 判断切分后子集大小，小于最小允许样本数停止切分3
    if (shape(mat0)[0] < tolN) or (shape(mat1)[0] < tolN):
        return None, leafType(dataSet)
    return bestIndex, bestValue                                              # 返回特征编号和用于切分的特征值


# 构建tree
def createTree(dataSet, leafType=regLeaf, errType=regErr, ops=(1,4)):
    # 数据集默认NumPy Mat 其他可选参数【结点类型：回归树，误差计算函数，ops包含树构建所需的其他元组】
    feat, val = chooseBestSplit(dataSet, leafType, errType, ops)
    if feat == None: return val                                             # 满足停止条件时返回叶结点值
    # 切分后赋值
    retTree = {}
    retTree['spInd'] = feat
    retTree['spVal'] = val
    # 切分后的左右子树
    lSet, rSet = binSplitDataSet(dataSet, feat, val)
    retTree['left'] = createTree(lSet, leafType, errType, ops)
    retTree['right'] = createTree(rSet, leafType, errType, ops)
    return retTree

# test
# myDat = mat(loadDataSet('ex00.txt'))
# print(createTree(myDat))
# myDat1 = mat(loadDataSet('ex0.txt'))
# print(createTree(myDat1))

# 画图（图1 + 图2）
# import matplotlib.pyplot as plt
# # myDat1 = mat(loadDataSet('ex00.txt'))
# # plt.plot(myDat1[:, 0], myDat1[:, 1], 'ro')
# myDat2 = mat(loadDataSet('ex0.txt'))
# plt.plot(myDat2[:, 1], myDat2[:, 2], 'ro')
# plt.show()


"""树剪枝
如果树节点过多，则该模型可能对数据过拟合，通过降低决策树的复杂度来避免过拟合的过程称为剪枝。在上面函数chooseBestSplit中
的三个提前终止条件是“预剪枝”操作，另一种形式的剪枝需要使用测试集和训练集，称作“后剪枝”。使用后剪枝方法需要将数据集
交叉验证，首先给定参数，使得构建出的树足够复杂，之后从上而下找到叶节点，判断合并两个叶节点是否能够取得更好的测试误差，
如果是就合并
"""


# 判断输入是否为一棵树
def isTree(obj):
    return (type(obj).__name__ == 'dict')       # 判断为字典类型返回true


# 返回树的平均值
def getMean(tree):
    if isTree(tree['right']):
        tree['right'] = getMean(tree['right'])
    if isTree(tree['left']):
        tree['left'] = getMean(tree['left'])
    return (tree['left'] + tree['right']) / 2.0


# 树的后剪枝
def prune(tree, testData):                                  # 待剪枝的树和剪枝所需的测试数据
    if shape(testData)[0] == 0: return getMean(tree)        # 确认数据集非空
    # 假设发生过拟合，采用测试数据对树进行剪枝
    if (isTree(tree['right']) or isTree(tree['left'])):     # 左右子树非空
        lSet, rSet = binSplitDataSet(testData, tree['spInd'], tree['spVal'])
    if isTree(tree['left']): tree['left'] = prune(tree['left'], lSet)
    if isTree(tree['right']): tree['right'] = prune(tree['right'], rSet)
    # 剪枝后判断是否还是有子树
    if not isTree(tree['left']) and not isTree(tree['right']):
        lSet, rSet = binSplitDataSet(testData, tree['spInd'], tree['spVal'])
        # 判断是否merge
        errorNoMerge = sum(power(lSet[:, -1] - tree['left'], 2)) + \
                       sum(power(rSet[:, -1] - tree['right'], 2))
        treeMean = (tree['left'] + tree['right']) / 2.0
        errorMerge = sum(power(testData[:, -1] - treeMean, 2))
        # 如果合并后误差变小
        if errorMerge < errorNoMerge:
            print("merging")
            return treeMean
        else:
            return tree
    else:
        return tree

# 创建所有可能中最大的树
# myMat2 = mat(loadDataSet('ex2.txt'))
# myTree = createTree(myMat2, ops=(0, 1))
# # 导入测试数据，执行剪枝过程
# myMat2Test = mat(loadDataSet('ex2test.txt'))
# prune(myTree, myMat2Test)
# print(myTree)


"""模型树 
采用树结构对数据建模，除了将叶节点设定为常数，也可将其设为分段线性函数
"""


# 模型树
def linearSolve(dataSet):                   # 将数据集格式化为X Y
    m, n = shape(dataSet)
    X = mat(ones((m, n)))
    Y = mat(ones((m, 1)))
    X[:, 1:n] = dataSet[:, 0:n - 1]
    Y = dataSet[:, -1]
    xTx = X.T * X
    if linalg.det(xTx) == 0.0:              # X Y用于简单线性回归，需要判断矩阵可逆
        raise NameError('This matrix is singular, cannot do inverse,\n\
        try increasing the second value of ops')
    ws = xTx.I * (X.T * Y)
    return ws, X, Y


def modelLeaf(dataSet):                     # 不需要切分时生成模型树叶节点
    ws, X, Y = linearSolve(dataSet)
    return ws                               # 返回回归系数


def modelErr(dataSet):                      # 用来计算误差找到最佳切分
    ws, X, Y = linearSolve(dataSet)
    yHat = X * ws
    return sum(power(Y - yHat, 2))

# test
# myMat2 = mat(loadDataSet(('exp2.txt')))
# myTree = createTree(myMat2, modelLeaf, modelErr, (1, 10))
# print(myTree)


"""树回归和标准回归的比较 
函数treeForeCast自顶向下遍历整棵树，直到命中叶节点为止。一旦到达叶节点，它会在输入数据上调用modelEval，该参数默认值是
regTreeEval。要对回归树叶节点预测，就调用regTreeEval，要对模型树节点预测，调用modelTreeEval
"""


# 用树回归进行预测
# 1-回归树
def regTreeEval(model, inDat):
    return float(model)


# 2-模型树
def modelTreeEval(model, inDat):
    n = shape(inDat)[1]
    X = mat(ones((1, n + 1)))
    X[:, 1:n + 1] = inDat
    return float(X * model)


# 对于输入的单个数据点，treeForeCast返回一个预测值。
def treeForeCast(tree, inData, modelEval=regTreeEval):      # 指定树类型
    if not isTree(tree): return modelEval(tree, inData)
    if inData[tree['spInd']] > tree['spVal']:
        if isTree(tree['left']):                            # 有左子树 递归进入子树
            return treeForeCast(tree['left'], inData, modelEval)
        else:                                               # 不存在子树 返回叶节点
            return modelEval(tree['left'], inData)
    else:
        if isTree(tree['right']):
            return treeForeCast(tree['right'], inData, modelEval)
        else:
            return modelEval(tree['right'], inData)


# 对数据进行树结构建模
def createForeCast(tree, testData, modelEval=regTreeEval):
    m = len(testData)
    yHat = mat(zeros((m, 1)))
    for i in range(m):
        yHat[i, 0] = treeForeCast(tree, mat(testData[i]), modelEval)
    return yHat


"""树回归与标准回归比较（相关系数 越接近1.0 越好）"""

# # 1.创建回归树
# trainMat = mat(loadDataSet('bikeSpeedVsIq_train.txt'))
# testMat = mat(loadDataSet('bikeSpeedVsIq_test.txt'))
# myTree1 = createTree(trainMat, ops=(1, 20))
# yHat1 = createForeCast(myTree1, testMat[:, 0])
# print(corrcoef(yHat1, testMat[:, 1], rowvar=0)[0, 1])
#
# # 2.创建一颗模型树【模型树误差更小（更加接近1.0）】
# myTree2 = createTree(trainMat, modelLeaf, modelErr, (1, 20))
# yHat2 = createForeCast(myTree2, testMat[:, 0], modelTreeEval)
# print(corrcoef(yHat2, testMat[:, 1], rowvar=0)[0, 1])
#
# # 3.标准线性回归
# ws, X, Y = linearSolve(trainMat)
# print(ws)
# m = shape(testMat)[0]
# yHat3 = mat(zeros((m, 1)))
# for i in range(m):
#     yHat3[i] = testMat[i, 0] * ws[1, 0] + ws[0, 0]
# print(corrcoef(yHat3, testMat[:, 1], rowvar=0)[0, 1])
