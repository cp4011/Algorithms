from numpy import *
from os import listdir


# k-近邻算法
def classify0(inputX, dataSet, labels, k):
    dataSetSize = dataSet.shape[0]
    diffMat = tile(inputX, (dataSetSize, 1)) - dataSet                        # numpy.tile()复制
    distances = (diffMat**2).sum(axis=1)**0.5                                 # 计算欧式距离(（x1-x2)^2 + (y1-y2)^2)^0.5
    sortedDistances = distances.argsort()                                     # 将矩阵的每一行向量相加: sum(a,axis=1)或a.sum(axis=1)
    classCount = {}
    for i in range(k):
        y = labels[sortedDistances[i]]
        classCount[y] = classCount.get(y, 0) + 1                              # dict.get(key, default=none）
    result = sorted(classCount.items(), key=lambda x: x[1], reverse=True)     # d.items()返回的是一个列表,如[('a',74), ('b',90)]
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
    returnMat = zeros((numberOfLines, 3))
    classLabelVector = []
    index = 0
    for line in arrayOLines:
        line = line.strip()                                               # 截取掉头尾的所有的回车字符和空格
        listFromLine = line.split('\t')
        returnMat[index] = listFromLine[0:3]
        classLabelVector.append(int(listFromLine[-1]))                    # 错classLabelVector = listFromLine[-1]
        index += 1
    return returnMat, classLabelVector


# 归一化特征值 newValue = (oldValue - min)/(max - min)
def autoNorm(dataSet):
    minValues = dataSet.min(0)                                            # 参数0使得函数从列中取得最小值，得到1 * 3 的向量
    maxVelues = dataSet.max(0)
    ranges = maxVelues - minValues
    returnNorm = zeros(shape(dataSet))
    m = len(dataSet)
    minValueMatrix = tile(minValues, (m, 1))                              # 复制1*3的向量minValues成m行1列
    rangesMatrix = tile(ranges, (m, 1))
    returnNorm = dataSet - minValueMatrix
    normDataSet = returnNorm / rangesMatrix
    return normDataSet, ranges, minValues                                  # 可以只返回归一化的结果normDataSet


# 分类器针对约会网站的测试代码
def datingClassTest():
    ratio = 0.5
    datingDataMat, datingLabels = file2matrix('datingTestSet2.txt')
    normMat, ranges, minVals = autoNorm(datingDataMat)
    m = normMat.shape[0]
    num = int(m * ratio)
    errorCount = 0.0
    for i in range(num):
        # 错classifierResult = classify0(normMat[i, :], normMat[num, :], datingLabels[num, :], 3)
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
    print("You will probably like this person:",resultList[result - 1])


# KNN识别手写数据集（32*32转换成1*1024的向量）
def img2vector(filename):
    returnVect = zeros((1, 1024))                                        #注意有两个()
    f = open(filename)
    for i in range(32):
        lineStr = f.readline()
        for j in range(32):
            returnVect[0, 32*i+j] = int(lineStr[j])                     # 存储在1*1024的Numpy的数组中
    return returnVect


def handWritingClassTest():
    hwLabels = []
    trainingFileList = listdir('trainingDigits')
    m = len(trainingFileList)
    trainingMat = zeros((m,1024))
    for i in range(m):
        fileNameStr = trainingFileList[i]
        a = fileNameStr.strip('.')[0]
        b = int(a.strip('_')[0])                                        # 注意要将字符int()一下
        hwLabels.append(b)
        trainingMat[i, :] = img2vector('trainingDigits/%s' % fileNameStr)
    testFileList = listdir('testDigits')
    mTest = len(testFileList)
    errorCount = 0.0
    for i in range(mTest):
        fileNameStr = testFileList[i]
        a = fileNameStr.strip('.')[0]
        b = int(a.strip('_')[0])
        vectorUnderTest = img2vector('testDigits/%s' % fileNameStr)
        classifierResult = classify0(vectorUnderTest, trainingMat, hwLabels, 3)
        # print("the classifier came back with: %d, the real answer is: %d" % (classifierResult, b))
        if classifierResult != b:
            errorCount += 1.0
    print("the total number of errors is: %d" % errorCount)
    print("the total error rate is: %f" % (errorCount / float(mTest)))


if __name__ == "__main__":
    handWritingClassTest()

