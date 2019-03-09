from numpy import *
from numpy import linalg as la


def loadExData():
    return [[0, 0, 0, 2, 2],
            [0, 0, 0, 3, 3],
            [0, 0, 0, 1, 1],
            [1, 1, 1, 0, 0],
            [2, 2, 2, 0, 0],
            [5, 5, 5, 0, 0],
            [1, 1, 1, 0, 0]]

def loadExData2():
    return [[0, 0, 0, 0, 0, 4, 0, 0, 0, 0, 5],
            [0, 0, 0, 3, 0, 4, 0, 0, 0, 0, 3],
            [0, 0, 0, 0, 4, 0, 0, 1, 0, 4, 0],
            [3, 3, 4, 0, 0, 0, 0, 2, 2, 0, 0],
            [5, 4, 5, 0, 0, 0, 0, 5, 5, 0, 0],
            [0, 0, 0, 0, 5, 0, 1, 0, 0, 5, 0],
            [4, 3, 4, 0, 0, 0, 0, 5, 5, 0, 1],
            [0, 0, 0, 4, 0, 4, 0, 0, 0, 0, 4],
            [0, 0, 0, 2, 0, 2, 5, 0, 0, 1, 2],
            [0, 0, 0, 0, 5, 0, 0, 0, 0, 4, 0],
            [1, 0, 0, 0, 0, 0, 0, 1, 2, 0, 0]]


# 欧式距离相似度： 1/(1+距离)
def ecludeSim(inA, inB):            # inA inB 都是列向量
    return 1.0 / 1.0 + la.norm(inA - inB)


# 余弦相似度
def cosSim(inA, inB):
    num = float(inA.T * inB)
    denom = la.norm(inA) * la.norm(inB)
    return 0.5 + 0.5 * (num /denom)


# 皮尔逊距离相关系数
def pearsSim(inA, inB):
    if len(inA) < 3:    # 检查是否存在3个或更多的点，如果不存在，函数返回1.0，因为此时两个向量完成相关
        return 1.0
    return 0.5 + 0.5 * corrcoef(inA, inB, rowvar=0)[0][1]


# 基于物品相似度的推荐引擎
def standEst(dataMat, user, simMeas, item):     # 数据矩阵、用户编号、相似度计算方法和物品编号
    n = shape(dataMat)[1]
    simTotal, ratSimTotal = 0.0, 0.0
    for j in range(n):
        userRating = dataMat[user, j]
        if userRating == 0:
            continue
        overLap = nonzero(logical_and(dataMat[:, item] > 0, dataMat[:, j].A > 0))[0]     # 寻找两个用户都做了评价的产品
        if  len(overLap) == 0:
            similarity = 0
        else:                                    # 存在两个用户都评价的产品 计算相似度
            similarity = simMeas(dataMat[overLap, item], dataMat[overLap, j])
        print("the %d and %d similarity is: %f" % (item, j, similarity))
        simTotal += similarity                   # 计算每个用户对所有评价产品累计相似度
        ratSimTotal += similarity * userRating   # 根据评分计算比率
    if simTotal == 0:
        return 0
    else:
        return ratSimTotal / simTotal


# 推荐引擎：产生最高的N个推荐结果
def recommend(dataMat, user, N=3, simMeas=cosSim, estMethod=standEst):
    unRatedItem = nonzero(dataMat[user, :].A == 0)[1]        # 寻找用户未评级的物品
    if len(unRatedItem) == 0:
        return "you rated everything"
    itemScores = []
    for item in unRatedItem:
        estimatedScore = estMethod(dataMat, user, simMeas, item)        # 基于相似度的评分
        itemScores.append((item, estimatedScore))
    return sorted(itemScores, key=lambda x: x[1], reverse=True)[:N]     # 返回前N个未评级的物品

# test
# myMat = mat(loadExData())
# myMat[0, 1] = myMat[0, 0] = myMat[1, 0] = myMat[2, 0] = 4
# myMat[3, 3] = 2
# print(recommend(myMat, 2))


# 利用SVD将11维的矩阵转化成3维的矩阵（3维已经达到总能力的90%以上信息）
def svdEst(dataMat, user, simMeas, item):
    n = shape(dataMat)[1]
    simTotal, ratSimTotal = 0.0, 0.0
    U, Sigma, VT = la.svd(dataMat)          # SVD分解
    Sig4 = mat(eye(4) * Sigma[:4])          # 建立对角矩阵
    xformedItems = dataMat.T * U[:, :4] * Sig4.I        # 降维：变换到低维空间
    for j in range(n):                      # 计算相似度，给出归一化评分
        userRating = dataMat[user, j]
        if userRating == 0 or j == item:
            continue
        similarity = simMeas(xformedItems[item, :].T, xformedItems[j, :].T)
        print("the %d and %d similarity is: %f" % (item, j, similarity))
        simTotal += similarity
        ratSimTotal += similarity * userRating
    if simTotal == 0:
        return 0
    else:
        return ratSimTotal / simTotal


# test
# myMat = mat(loadExData2())
# # print(recommend(myMat, 1, estMethod=svdEst))         # 默认余弦相似度
# print(recommend(myMat, 1, estMethod=svdEst, simMeas=ecludeSim))    # 欧氏距离相似度


# SVD实现图像压缩
# 打印矩阵: 由于矩阵包含了浮点数,因此必须定义浅色和深色。
def printMat(inMat, thresh=0.8):
    for i in range(32):
        for j in range(32):
            if float(inMat[i,j]) > thresh:
                print("1", end=" ")
            else: print("0", end=" ")
        print ('')


# 压缩
def imgCompress(numSV=3, thresh=0.8):
    myl = []
    for line in open('0_5.txt').readlines():
        newRow = []
        for i in range(32):
            newRow.append(int(line[i]))
        myl.append(newRow)
    myMat = mat(myl)
    print("****original matrix******")
    printMat(myMat, thresh)
    U, Sigma, VT = la.svd(myMat)                    # SVD分解得到特征矩阵
    SigRecon = mat(zeros((numSV, numSV)))           # 初始化新对角矩阵
    for k in range(numSV):                          # 构造对角矩阵，将特征值填充到对角线
        SigRecon[k, k] = Sigma[k]
    reconMat = U[:, :numSV]*SigRecon*VT[:numSV, :]    # 降维
    print("****reconstructed matrix using %d singular values******" % numSV)
    printMat(reconMat, thresh)

#test
imgCompress(2)
