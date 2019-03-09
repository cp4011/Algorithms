from numpy import *


def loadDataSet(fileName, delim='\t'):
    fr = open(fileName)
    stringArr = [line.strip().split(delim) for line in fr.readlines()]
    dataArr = [list(map(float, line)) for line in stringArr]    # 在Python3中map()函数返回迭代器，需要在map()函数前加上list()将结果转为列表，
    return mat(dataArr)


def PCA(dataMat, topNfeat = 99999):                         # topNfeat需要保留的特征维度,默认99999
    meanVals = mean(dataMat, axis=0)                        # 求数据矩阵每一列的均值
    meanRemoved = dataMat - meanVals                        # 数据矩阵每一列特征减去该列的特征均值remove mean
    covMat = cov(meanRemoved, rowvar=0)                     # 计算协方差矩阵，除数n-1是为了得到协方差的无偏估计，
    # cov(X,0) = cov(X)除数是n-1(n为样本个数)；cov(X,1)除数是n
    eigVals, eigVects = linalg.eig(mat(covMat))             # 计算协方差矩阵的特征值及对应的特征向量
    eigValInd = argsort(eigVals)                            # argsort():对特征值矩阵进行由小到大排序，返回对应排序后的索引
    eigValInd = eigValInd[:-(topNfeat + 1):-1]              # 从排序后的矩阵最后一个开始自下而上选取最大的N个特征值，返回其对应的索引
    redEigVects = eigVects[:, eigValInd]                    # 将特征值最大的N个特征值对应索引的特征向量提取出来，组成压缩矩阵
    lowDDataMat = meanRemoved * redEigVects                 # 将去除均值后的数据矩阵*压缩矩阵，转换到新的空间，使维度降低为N
    reconMat = (lowDDataMat * redEigVects.T) + meanVals     # 利用降维后的矩阵反构出原数据矩阵(用作测试，可跟未压缩的原矩阵比对)
    return lowDDataMat, reconMat                            # 返回压缩后的数据矩阵和该矩阵反构出原始数据矩阵


# test
dataMat = loadDataSet('testSet.txt')
lowDMat, reconMat = PCA(dataMat, 1)
print(lowDMat.shape)
import matplotlib.pyplot as plt
fig = plt.figure()
ax = fig.add_subplot(111)
ax.scatter(dataMat[:, 0].tolist(), dataMat[:, 1].tolist(), marker='^', s=90)                # 三角形表示原始数据点
ax.scatter(reconMat[:, 0].tolist(), reconMat[:, 1].tolist(), marker='o', s=50, c='red')     # 圆形点表示第一主成分点，点颜色为红色
plt.show()


# 利用PCA对半导体制造数据降维
def replaceNanWithMean():
    datMat = loadDataSet('secom.data', ' ')
    numFeat = shape(datMat)[1]      # 计算出特征的数目
    for i in range(numFeat):        # 对每个特征                          # matrix.A 将矩阵转换为 数组array
        meanVal = mean(datMat[nonzero(~isnan(datMat[:, i].A))[0], i])     # 计算所有非NaN的平均值，缺失值NaN (Not a number)
        datMat[nonzero(isnan(datMat[:, i].A))[0], i] = meanVal            # 将所有NaN置为平均值
    return datMat


# test
dataMat = replaceNanWithMean()
lowDMat, reconMat = PCA(dataMat, 6)     # 可以打印出中间的eigVals查看，6个主要成分已经占96.8%的累积方差百分比
print(lowDMat.shape)
