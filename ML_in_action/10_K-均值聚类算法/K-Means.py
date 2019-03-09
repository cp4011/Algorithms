from numpy import *


def loadDataSet(fileName):
    dataMat = []
    fr = open(fileName)
    for line in fr.readlines():                     # for each line
        curLine = line.strip().split('\t')
        fltLine = list(map(float, curLine))         # 加list()转换成 列表
        dataMat.append(fltLine)
    return dataMat


# 欧氏距离
def distEclud(vecA, vecB):
    return sqrt(sum(power(vecA - vecB, 2)))      # la.norm(vecA-vecB) 两向量A B的欧式距离


# init K points randomly
def randCent(dataSet, k):
    dataSet = mat(dataSet)                       # list要转成矩阵, dataset矩阵内部数据如：[[x1,y1],[x2,y2],...]
    n = shape(dataSet)[1]                        # 坐标点的列数（维数），如二维（x,y)
    centroids = mat(zeros((k, n)))               # create centroid mat
    for j in range(n):                           # 随机初始化簇中心（j先对第一列，即x坐标；j再对第二列，即y坐标初始化）
        minJ = min(dataSet[:, j])                                   # 取众多样本点的x坐标所形成的第一列x1,x2...中 的最小值
        rangeJ = float(max(dataSet[:, j]) - minJ)                   # 找到x坐标列中的 range
        centroids[:, j] = mat(minJ + rangeJ * random.rand(k, 1))    # 随机初始化k个中心点中的 x（或y）：范围是在样本点中
    return centroids                                                # np.random.rand() 取值范围[0,1）


# K-均值算法: 采用计算质心-分配-重新计算质心反复迭代的方式，直到所有点的分配结果不再改变。设置flag为clusterChange=True
def kMeans(dataSet, k, distMeas=distEclud, createCent=randCent):    # 参数：dataset,num of cluster,distance func,initCen
    dataSet = mat(dataSet)                     # list转成矩阵
    m = shape(dataSet)[0]                      # 行数（有多少个样本点）
    clusterAssment = mat(zeros((m, 2)))        # store the result matrix,2 cols for index(中心点的标号) and error
    centroids = createCent(dataSet, k)
    clusterChanged = True
    while clusterChanged:
        clusterChanged = False
        for i in range(m):                                  # for every points
            minDist = inf                                   # 无穷大
            minIndex = -1
            for j in range(k):                              # for every k centers，find the nearest center
                distJI = distMeas(centroids[j, :], dataSet[i, :])
                if distJI < minDist:                        # if distance is shorter than minDist
                    minDist, minIndex = distJI, j           # update distance and 中心点j
            if clusterAssment[i, 0] != minIndex:
                clusterChanged = True   # 此处判断数据点所属类别与之前是否变化，只要有一个点变化就重设为True，再次迭代
            clusterAssment[i, :] = minIndex, minDist**2     # 第i个样本点遍历完与k个中心点的距离后，记录下该之距离最近的中心点和误差（其距离的平方）
        for cent in range(k):                               # 对每个中心点（更新每个中心点）
            ptsInClust = dataSet[nonzero(clusterAssment[:, 0].A == cent)[0]]    # 取出属于这个中心点的所有非0数据点，并取第一维的索引（行）
            centroids[cent, :] = mean(ptsInClust, axis=0)
    return centroids, clusterAssment
# test
# datMat = loadDataSet('testSet.txt')
# myCentroids, clustAssing = kMeans(datMat, 4)
# print(myCentroids)


# 二分K-均值聚类
def biKmeans(dataSet, k, distMeas=distEclud):
    dataSet = mat(dataSet)                              # list要转成matrix
    m = shape(dataSet)[0]
    clusterAssment = mat(zeros((m, 2)))
    centroid0 = mean(dataSet, axis=0).tolist()[0]       # 整个样本集的中心点
    centList = [centroid0]                              # create a list with one centroid
    for j in range(m):                                  # calc initial Error for each point
        clusterAssment[j, 1] = distMeas(mat(centroid0), dataSet[j, :]) ** 2     # 遍历所有点计算该点到质心的误差（距离平方）
    while (len(centList) < k):                          # 当簇数目小于要划分的k时
        lowestSSE = inf                                 # init SSE 无穷大
        for i in range(len(centList)):                  # for every centroid(尝试划分每一簇，最后选择划分最大程度降低误差SSE的那一簇）
            ptsInCurrCluster = dataSet[nonzero(clusterAssment[:, 0].A == i)[0], :]  # get the data points currently in cluster i
            centroidMat, splitClustAss = kMeans(ptsInCurrCluster, 2, distMeas)      # k=2, kMeans
            sseSplit = sum(splitClustAss[:, 1])         # compare the SSE to the currrent minimum
            sseNotSplit = sum(clusterAssment[nonzero(clusterAssment[:, 0].A != i)[0], 1])
            print("sseSplit, and notSplit: ", sseSplit, sseNotSplit)
            if (sseSplit + sseNotSplit) < lowestSSE:    # judge the error
                bestCentToSplit = i                     # 记录簇i（将要划分该簇：因为划分该簇 会最大程度降低SSE误差平方和）
                bestNewCents = centroidMat              # 记录该簇后的质心点矩阵
                bestClustAss = splitClustAss.copy()     # 复制矩阵（每个点簇分配结果和对应的误差）
                lowestSSE = sseSplit + sseNotSplit      # 记录划分该簇后的误差
        # new cluster and split cluster
        bestClustAss[nonzero(bestClustAss[:, 0].A == 1)[0], 0] = len(centList)       # 从1到 3,4，5...（目前总共划分到几个簇了）
        bestClustAss[nonzero(bestClustAss[:, 0].A == 0)[0], 0] = bestCentToSplit     # 最佳划分簇i，第一次是0（因为划分的就是 簇0）
        print('the bestCentToSplit is: ', bestCentToSplit)                           # 第一次划分的是 0
        print('the len of bestClustAss is: ', len(bestClustAss))                     # 最佳划分簇i，第一次打印的是 1
        centList[bestCentToSplit] = bestNewCents[0, :].tolist()[0]   # replace a centroid with two best centroids（最初的centroid0被更新了）
        centList.append(bestNewCents[1, :].tolist()[0])              # 并append添加了刚划分出来的另外一个centrios（说明以后每次划分都会增加一个）
        clusterAssment[nonzero(clusterAssment[:, 0].A == bestCentToSplit)[0], :] = bestClustAss  # reassign new clusters, and SSE
    return mat(centList), clusterAssment            # 返回 质心列表， 簇分配结果
# test
# datMat3 = loadDataSet('testSet2.txt')
# centList, myNewAssment = biKmeans(datMat3, 3)
# print(centList)

# practice example
# 地址转换成对应的经纬度（雅虎Yahoo的API）[PortlandClubs.txt转化成places.txt]  ***见最后***


# distance calc function：结合两个点经纬度（用角度做单位），返回地球表面两点之间距离
def distSLC(vecA, vecB):            # 球面余弦定理 Spherical Law of Cosines
    a = sin(vecA[0, 1]*pi/180) * sin(vecB[0, 1]*pi/180)     # sin前需要将 角度转换成弧度
    b = cos(vecA[0, 1]*pi/180) * cos(vecB[0, 1]*pi/180) * cos(pi * (vecB[0, 0]-vecA[0, 0]) / 180)
    return arccos(a + b)*6371.0     # pi is imported with numpy


# draw function
import matplotlib.pyplot as plt
def clusterClubs(numClust=5):       # 参数：希望得到的簇数目
    datList = []
    for line in open('places.txt').readlines():                 # 获取地图数据
        lineArr = line.split('\t')
        datList.append([float(lineArr[4]), float(lineArr[3])])  # 逐个获取第四列和第五列的经纬度信息
    datMat = mat(datList)
    myCentroids, clustAssing = biKmeans(datMat, numClust, distMeas=distSLC)
    # draw
    fig = plt.figure()
    rect = [0.1, 0.1, 0.8, 0.8]                                             # 创建矩形
    scatterMarkers = ['s', 'o', '^', '8', 'p', 'd', 'v', 'h', '>', '<']     # 创建不同标记图案
    axprops = dict(xticks=[], yticks=[])
    ax0 = fig.add_axes(rect, label='ax0', **axprops)
    imgP = plt.imread('Portland.png')                                       # 导入地图
    ax0.imshow(imgP)
    ax1 = fig.add_axes(rect, label='ax1', frameon=False)
    for i in range(numClust):
        ptsInCurrCluster = datMat[nonzero(clustAssing[:, 0].A == i)[0], :]
        markerStyle = scatterMarkers[i % len(scatterMarkers)]
        ax1.scatter(ptsInCurrCluster[:, 0].flatten().A[0], ptsInCurrCluster[:, 1].flatten().A[0], marker=markerStyle, s=90)
    ax1.scatter(myCentroids[:, 0].flatten().A[0], myCentroids[:, 1].flatten().A[0], marker='+', s=300)      # 画中心点（散点）
    plt.show()
# test
# clusterClubs(5)


# 地址转换成对应的经纬度（雅虎Yahoo的API）[PortlandClubs.txt转化成places.txt]
import urllib
import json
def geoGrab(stAddress, city):
    apiStem = 'http://where.yahooapis.com/geocode?'     # create a dict and constants for the goecoder
    params = {}
    params['flags'] = 'J'                               # JSON return type
    params['appid'] = 'aaa0VN6k'
    params['location'] = '%s %s' % (stAddress, city)
    url_params = urllib.urlencode(params)
    yahooApi = apiStem + url_params                     # print url_params
    print(yahooApi)
    c = urllib.urlopen(yahooApi)
    return json.loads(c.read())


from time import sleep
def massPlaceFind(fileName):
    fw = open('places.txt', 'w')                    # 写文件
    for line in open(fileName).readlines():
        line = line.strip()
        lineArr = line.split('\t')
        retDict = geoGrab(lineArr[1], lineArr[2])
        if retDict['ResultSet']['Error'] == 0:      # 返回的字典 没出错
            lat = float(retDict['ResultSet']['Results'][0]['latitude'])          # 解析得到 经纬度
            lng = float(retDict['ResultSet']['Results'][0]['longitude'])         # 字符串要转换成浮点数 float()
            print("%s\t%f\t%f" % (lineArr[0], lat, lng))
            fw.write('%s\t%f\t%f\n' % (line, lat, lng))                          # 写入
        else:
            print("error fetching")
        sleep(1)            # 延迟1秒，频繁调用API，可能会被封掉
    fw.close()              # 写入后记得： fw.close()



