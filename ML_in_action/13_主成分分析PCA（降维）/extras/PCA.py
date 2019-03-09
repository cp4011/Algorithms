from numpy import *


def loadDataSet(fileName, delim='\t'):
    fr = open(fileName)
    stringArr = [line.strip().split(delim) for line in fr.readlines()]
    dataArr = [list(map(float, line)) for line in stringArr]    # 在Python3中map()函数返回迭代器，需要在map()函数前加上list()将结果转为列表，
    return mat(dataArr)


def PCA(dataMat, topNfeat = 9999999):
    meanVals = mean(dataMat, axis=0)
    meanRemoved = dataMat - meanVals                        # remove mean
    covMat = cov(meanRemoved, rowvar=0)
    eigVals, eigVects = linalg.eig(mat(covMat))
    eigValInd = argsort(eigVals)                            # sort, sort goes smallest to largest
    eigValInd = eigValInd[:-(topNfeat + 1):-1]              # cut off unwanted dimensions
    redEigVects = eigVects[:, eigValInd]                    # reorganize eig vects largest to smallest
    lowDDataMat = meanRemoved * redEigVects                 # transform data into new dimensions
    reconMat = (lowDDataMat * redEigVects.T) + meanVals
    return lowDDataMat, reconMat
# test
# dataMat = loadDataSet('testSet.txt')
# lowDMat, reconMat = PCA(dataMat, 1)
# print(lowDMat.shape)


def replaceNanWithMean():
    datMat = loadDataSet('secom.data', ' ')
    numFeat = shape(datMat)[1]
    for i in range(numFeat):
        meanVal = mean(datMat[nonzero(~isnan(datMat[:, i].A))[0], i])     # values that are not NaN (a number)
        datMat[nonzero(isnan(datMat[:, i].A))[0], i] = meanVal    # set NaN values to mean
    return datMat
