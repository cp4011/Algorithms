from numpy import *
from os import listdir

"""k-近邻算法
优点：精度高、对异常值不敏感、无数据输入假定。
缺点：计算复杂度高、空间复杂度高。
使用数据范围：数值型和标称型。

伪代码： 
对未知类别属性的数据集中的每个点依次执行以下操作：
(1).计算已知类别数据集中的点与当前点之间的距离；
(2).按照距离递增次序排序；
(3).选取与当前点距离最小的k个点；
(4).确定前k个点所在类别的出现频率；
(5).返回前k个点出现频率最高的类别作为当前点的预测分类。
"""


# k-近邻算法
def classify0(inputX, dataSet, labels, k):
    """
        Function：   创建数据集和标签

        Args：       inputX：用于分类的输入向量 (1xN)
                    dataSet：输入的训练样本集 (NxM)
                    labels：标签向量 (1xM vector)
                    k：用于比较的近邻数量 (should be an odd number)

        Returns：    sortedClassCount[0][0]：分类结果
    """
    # dataSet.shape[0]：求dataSet矩阵的行数
    # dataSet.shape[1]：求dataSet矩阵的列数
    # dataSet.shape：元组形式输出矩阵行数、列数
    dataSetSize = dataSet.shape[0]
    # tile(A, B)：将A重复B次，其中B可以是int类型也可以是元组类型
    # 这句话相当于向量inputX与矩阵dataSet里面的每组数据做差
    diffMat = tile(inputX, (dataSetSize, 1)) - dataSet                        # numpy.tile()复制
    # sqDiffMat.sum(axis=0)：对矩阵的每一列求和
    # sqDiffMat.sum(axis=1)：对矩阵的每一行求和
    # sqDiffMat.sum()：对整个矩阵求和
    distances = (diffMat**2).sum(axis=1)**0.5                                 # 计算欧式距离(（x1-x2)^2 + (y1-y2)^2)^0.5
    sortedDistances = distances.argsort()   # 返回从小到大排序的索引          # 将矩阵的每一行向量相加: sum(a,axis=1)或a.sum(axis=1)
    classCount = {}
    for i in range(k):                      # 给字典赋值
        y = labels[sortedDistances[i]]      # 字典的key
        classCount[y] = classCount.get(y, 0) + 1                              # dict.get(key, default=none）
    result = sorted(classCount.items(), key=lambda x: x[1], reverse=True)     # d.items()返回的是一个列表,如[('a',74), ('b',90)]
    # 返回可遍历的(键, 值) 元组数组,如[('Google', 3), ('taobao', 2), ('Runoob', 1)]
    return result[0][0]                                                       # 错误return result[0],这是返回的tuple


# 数据集举例
def createDataSet():
    group = array([[1.0, 1.1], [1.0, 1.0], [0, 0], [0, 0.1]])
    labels = ['A', 'A', 'B', 'B']
    return group, labels


# 准备数据：从文本文件中解析数据
def file2matrix(filename):
    f = open(filename)
    arrayOLines = f.readlines()
    numberOfLines = len(arrayOLines)
    returnMat = zeros((numberOfLines, 3))       # 创建返回的NumPy矩阵
    classLabelVector = []                       # 创建返回的向量列表
    index = 0
    for line in arrayOLines:
        line = line.strip()                                               # 截取掉头尾的所有的回车字符和空格
        listFromLine = line.split('\t')                                   # 使用tab字符将上一步得到的整行数据分割成一个元素列表
        returnMat[index] = listFromLine[0:3]                              # 选取前三个元素，存储到特征矩阵中
        classLabelVector.append(int(listFromLine[-1]))                    # 错classLabelVector = listFromLine[-1]
        index += 1
    return returnMat, classLabelVector                                    # 返回训练样本矩阵和类标签向量


# 归一化特征值 newValue = (oldValue - min)/(max - min)
def autoNorm(dataSet):
    # 求取列的最小值
    minValues = dataSet.min(0)                                            # 参数0使得函数从列中取得最小值，得到1 * 3 的向量
    maxVelues = dataSet.max(0)
    ranges = maxVelues - minValues
    returnNorm = zeros(shape(dataSet))                                    # 创建输出矩阵normDataSet
    m = len(dataSet)
    minValueMatrix = tile(minValues, (m, 1))                              # 复制1*3的向量minValues成m行1列
    rangesMatrix = tile(ranges, (m, 1))
    returnNorm = dataSet - minValueMatrix
    normDataSet = returnNorm / rangesMatrix
    # 返回归一化矩阵、差值向量和最小值向量
    return normDataSet, ranges, minValues                                  # 可以只返回归一化的结果normDataSet


# 分类器针对约会网站的测试代码
def datingClassTest():
    ratio = 0.5
    datingDataMat, datingLabels = file2matrix('datingTestSet2.txt')
    normMat, ranges, minVals = autoNorm(datingDataMat)      # 归一化特征值
    m = normMat.shape[0]
    num = int(m * ratio)                                    # 初始化测试向量个数
    errorCount = 0.0
    for i in range(num):                                    # 对测试集分类，返回分类结果并打印
        # 错classifierResult = classify0(normMat[i, :], normMat[num, :], datingLabels[num, :], 3)
        # 传参给分类器进行分类，每个for循环改变的参数只有第一项的测试数据而已
        classifierResult = classify0(normMat[i, :], normMat[num:m, :], datingLabels[num:m], 3)
        print("the classifier came back with: %d, the real answer is: %d" % (classifierResult, datingLabels[i]))
        if classifierResult != datingLabels[i]:
            errorCount += 1.0
    print("the errorCount is %d" % errorCount)
    print("the total error rate is: %f" % (errorCount / float(num)))            # 注意是%f, 而%d：0.066就输出为0


# KNN预测约会网站某人的喜欢程度
def classifyPerson():
    resultList = ['not at all', 'in small doses', 'in large doses']
    percentTats = float(input("percentage of time spent playing video games?\n"))
    ffMiles = float(input("frequent flier miles earned per year?\n"))
    iceCream = float(input("liters of ice cream consumed per year?\n"))
    inArr = array([percentTats, ffMiles, iceCream])                     # 注意要加上[]
    datingDataMat, datingLabels = file2matrix('datingTestSet2.txt')
    normMat, ranges, minValues = autoNorm(datingDataMat)
    result = classify0(inArr, normMat, datingLabels, 3)
    print("You will probably like this person:", resultList[result - 1])


# KNN识别手写数据集（32*32转换成1*1024的向量）
def img2vector(filename):
    returnVect = zeros((1, 1024))                                       # 注意有两个()
    f = open(filename)
    for i in range(32):
        lineStr = f.readline()
        for j in range(32):
            returnVect[0, 32*i+j] = int(lineStr[j])                     # 存储在1*1024的Numpy的数组中
    return returnVect                                                   # 返回要输出的1*1024向量


def handWritingClassTest():
    hwLabels = []
    trainingFileList = listdir('trainingDigits')    # os.listdir()用于返回指定的文件夹包含的文件或文件夹的名字的列表(以字母顺序)
    m = len(trainingFileList)                       # 获取训练文件数目
    trainingMat = zeros((m, 1024))                  # 初始化训练矩阵
    for i in range(m):                              # 开始提取训练集
        fileNameStr = trainingFileList[i]           # 从文件名列表中循环取各文件名
        a = fileNameStr.split('.')[0]               # 从文件名解析出分类数字
        b = int(a.split('_')[0])                    # 注意要将字符int()一下
        hwLabels.append(b)                          # 存储解析出的分类数字到标签中
        trainingMat[i, :] = img2vector('trainingDigits/%s' % fileNameStr)
    testFileList = listdir('testDigits')
    mTest = len(testFileList)
    errorCount = 0.0
    for i in range(mTest):
        fileNameStr = testFileList[i]
        a = fileNameStr.strip('.')[0]
        b = int(a.strip('_')[0])
        vectorUnderTest = img2vector('testDigits/%s' % fileNameStr)
        classifierResult = classify0(vectorUnderTest, trainingMat, hwLabels, 3)     # 参数传入分类器进行分类
        # print("the classifier came back with: %d, the real answer is: %d" % (classifierResult, b))
        if classifierResult != b:
            errorCount += 1.0
    print("the total number of errors is: %d" % errorCount)
    print("the total error rate is: %f" % (errorCount / float(mTest)))


if __name__ == "__main__":
    handWritingClassTest()

