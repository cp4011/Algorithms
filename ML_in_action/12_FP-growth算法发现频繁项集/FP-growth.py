"""FP-growth算法只需要对数据库进行两次扫描，而Apriori算法对于每个潜在的频繁项集都会扫描数据集判定给定模式是否频繁，
因此FP-growth算法的速度要比Apriori算法快。
它发现频繁项集的基本过程如下：
(1) 构建FP树
(2) 从FP树中挖掘频繁项集
"""


# FP树中节点的类定义
class treeNode:
    def __init__(self, nameValue, numCount, parentNode):
        self.name = nameValue
        self.count = numCount
        self.nodeLink = None        # nodeLink 变量用于链接相似的元素项
        self.parent = parentNode    # 通常（从上往下迭代访问节点）不需要该变量，但为后文：叶子结点上溯整棵树，需要指向父节点的指针
        self.children = {}          # 空字典，存放节点的子节点

    def inc(self, numOccur):        # inc()对变量count增加给定值
        self.count += numOccur

    def disp(self, ind=1):        # 将树以文本形式显示（方便调试）
        print(' '*ind, self.name, ' ', self.count)
        for child in self.children.values():
            child.disp(ind + 1)
# test
# rootNode = treeNode('pyramid', 9, None)
# rootNode.children['eye'] = treeNode('eye', 13, None)
# rootNode.children['phoenix'] = treeNode('phoenix', 3, None)
# rootNode.disp()


# 构建FP-tree
def createTree(dataSet, minSup=1):
    headerTable = {}
    for trans in dataSet:                   # 第一次遍历：统计各个数据的频繁度
        for item in trans:
            headerTable[item] = headerTable.get(item, 0) + dataSet[trans]
            # 用头指针表统计各个类别的出现的次数，计算频繁量：头指针表[类别]=出现次数
    for k in list(headerTable.keys()):      # 删除未达到最小频繁度的数据
        if headerTable[k] < minSup:
            del (headerTable[k])
    freqItemSet = set(headerTable.keys())   # 保存达到要求的数据
    # print ('freqItemSet: ',freqItemSet)
    if len(freqItemSet) == 0:
        return None, None                   # 若达到要求的数目为0
    for k in headerTable:                   # 遍历头指针表
        headerTable[k] = [headerTable[k], None]         # 保存计数值及指向每种类型第一个元素项的指针
    # print ('headerTable: ',headerTable)
    retTree = treeNode('Null Set', 1, None)             # 初始化tree
    for tranSet, count in dataSet.items():              # 第二次遍历：
        localD = {}
        for item in tranSet:                            # put transaction items in order
            if item in freqItemSet:                     # 只对频繁项集进行排序
                localD[item] = headerTable[item][0]

        # 使用排序后的频率项集对树进行填充
        if len(localD) > 0:
            orderedItems = [v[0] for v in sorted(localD.items(), key=lambda p: p[1], reverse=True)]
            updateTree(orderedItems, retTree, headerTable, count)  # populate tree with ordered freq itemset
    return retTree, headerTable                         # 返回树和头指针表


def updateTree(items, inTree, headerTable, count):
    if items[0] in inTree.children:                     # 首先检查是否存在该节点
        inTree.children[items[0]].inc(count)            # 存在则计数增加
    else:                                               # 不存在则将新建该节点
        inTree.children[items[0]] = treeNode(items[0], count, inTree)           # 创建一个新节点
        if headerTable[items[0]][1] == None:                                    # 若原来不存在该类别，更新头指针列表
            headerTable[items[0]][1] = inTree.children[items[0]]                # 更新指向
        else:                                                                   # 更新指向
            updateHeader(headerTable[items[0]][1], inTree.children[items[0]])
    if len(items) > 1:                                                          # 仍有未分配完的树，迭代
        updateTree(items[1::], inTree.children[items[0]], headerTable, count)


# 节点链接指向树中该元素项的每一个实例。
# 从头指针表的 nodeLink 开始,一直沿着nodeLink直到到达链表末尾
def updateHeader(nodeToTest, targetNode):
    while (nodeToTest.nodeLink != None):
        nodeToTest = nodeToTest.nodeLink
    nodeToTest.nodeLink = targetNode


def loadSimpDat():
    simpDat = [['r', 'z', 'h', 'j', 'p'],
               ['z', 'y', 'x', 'w', 'v', 'u', 't', 's'],
               ['z'],
               ['r', 'x', 'n', 'o', 's'],
               ['y', 'r', 'x', 'z', 'q', 't', 'p'],
               ['y', 'z', 'x', 'e', 'q', 's', 't', 'm']]
    return simpDat


# createInitSet() 用于实现上述从列表到字典的类型转换过程
def createInitSet(dataSet):
    retDict = {}
    for trans in dataSet:
        retDict[frozenset(trans)] = 1
    return retDict

# test
# simpDat = loadSimpDat()
# initSet = createInitSet(simpDat)
# print(initSet)
# myFPtree, myHeaderTab = createTree(initSet, 3)
# myFPtree.disp()


"""从 FP树 中挖掘频繁项集: 
(1) 从FP树中获得条件模式基;
(2) 利用条件模式基,构建一个条件FP树;                      
(3) 迭代重复步骤(1)步骤(2),直到树包含一个元素项为止。

条件模式基是以所查找元素项为结尾的路径集合。
每一条路径其实都是一条前缀路径(prefix path)。简而言之,一条前缀路径是介于所查找元素项与树根节点之间的所有内容
"""


# 从FP树中发现频繁项集
def ascendTree(leafNode, prefixPath):       # 递归上溯整棵树
    if leafNode.parent != None:
        prefixPath.append(leafNode.name)
        ascendTree(leafNode.parent, prefixPath)


def findPrefixPath(basePat, treeNode):      # 参数：指针，节点；
    condPats = {}
    while treeNode != None:
        prefixPath = []
        ascendTree(treeNode, prefixPath)    # 寻找当前非空节点的前缀
        if len(prefixPath) > 1:
            condPats[frozenset(prefixPath[1:])] = treeNode.count    # 将条件模式基添加到字典中
        treeNode = treeNode.nodeLink
    return condPats

# test
# simpDat = loadSimpDat()
# initSet = createInitSet(simpDat)
# myFPtree, myHeaderTab = createTree(initSet, 3)
# myFPtree.disp()
# print(findPrefixPath('x', myHeaderTab['x'][1]))
# print(findPrefixPath('z', myHeaderTab['z'][1]))
# print(findPrefixPath('r', myHeaderTab['r'][1]))


"""函数mineTree对参数inTree代表的FP树进行频繁项集挖掘。首先对headerTable中出现的单个元素按出现频率从小到大排序，之后将
每个元素的条件模式基作为输入数据，建立针对当前元素的条件树，如果生成的这棵条件树仍有元素，就在这棵条件树里寻找频繁项集，
因为prefix参数是在递归过程中不断向下传递的，因此由最初的headerTable中的某个元素x衍生出的所有频繁项集都带有x
"""


# 递归查找频繁项集
def mineTree(inTree, headerTable, minSup, preFix, freqItemList):
    # 头指针表中的元素项按照频繁度排序,从小到大
    bigL = [v[0] for v in sorted(headerTable.items(), key=lambda p: str(p[1]))]     # python3修改: str()
    for basePat in bigL:                    # 从底层开始
        newFreqSet = preFix.copy()
        newFreqSet.add(basePat)             # 加入频繁项列表
        # print ('finalFrequent Item: ',newFreqSet)
        freqItemList.append(newFreqSet)
        condPattBases = findPrefixPath(basePat, headerTable[basePat][1])     # 递归调用函数来创建基
        # print('condPattBases :',basePat, condPattBases)
        # 2.构建条件模式Tree
        myCondTree, myHead = createTree(condPattBases, minSup)               # 将创建的条件基作为新的数据集添加到fp-tree
        # print ('head from conditional tree: ', myHead)
        if myHead != None:                                                   # 3.递归
            # print('conditional tree for: ',newFreqSet)
            # myCondTree.disp(1)
            mineTree(myCondTree, myHead, minSup, newFreqSet, freqItemList)

# test
simpDat = loadSimpDat()
initSet = createInitSet(simpDat)
myFPtree, myHeaderTab = createTree(initSet, 3)
freqItems = []
mineTree(myFPtree, myHeaderTab, 3, set([]), freqItems)
print(freqItems)


"""在FP-growth算法中,数据集存储在一个称为FP树的结构中。FP树构建完成后,可以通过查找元素项的条件基及构建条件FP树来发现频繁
项集。该过程不断以更多元素作为条件重复进行,直到FP树只包含一个元素为止.可以使用FP-growth算法在多种文本文档中查找频繁单词。
"""


# 在Twitter源中发现一些共现词
import twitter
from time import sleep
import re


# 访问Twitter Python库的代码
def getLotsOfTweets(searchStr):
    CONSUMER_KEY = ''
    CONSUMER_SECRET = ''
    ACCESS_TOKEN_KEY = ''
    ACCESS_TOKEN_SECRET = ''
    api = twitter.Api(consumer_key=CONSUMER_KEY, consumer_secret=CONSUMER_SECRET,
                      access_token_key=ACCESS_TOKEN_KEY,
                      access_token_secret=ACCESS_TOKEN_SECRET)
    # you can get 1500 results 15 pages * 100 per page
    resultsPages = []
    for i in range(1, 15):
        print("fetching page %d" % i)
        searchResults = api.GetSearch(searchStr, per_page=100, page=i)
        resultsPages.append(searchResults)
        sleep(6)
    return resultsPages


# 文本解析及合成代码
def textParse(bigString):
    urlsRemoved = re.sub('(http:[/][/]|www.)([a-z]|[A-Z]|[0-9]|[/.]|[~])*', '', bigString)
    listOfTokens = re.split(r'\W*', urlsRemoved)
    return [tok.lower() for tok in listOfTokens if len(tok) > 2]



def mineTweets(tweetArr, minSup=5):
    parsedList = []
    for i in range(14):
        for j in range(100):
            parsedList.append(textParse(tweetArr[i][j].text))
    initSet = createInitSet(parsedList)
    myFPtree, myHeaderTab = createTree(initSet, minSup)
    myFreqList = []
    mineTree(myFPtree, myHeaderTab, minSup, set([]), myFreqList)
    return myFreqList

# minSup = 3
# simpDat = loadSimpDat()
# initSet = createInitSet(simpDat)
# myFPtree, myHeaderTab = createTree(initSet, minSup)
# myFPtree.disp()
# myFreqList = []
# mineTree(myFPtree, myHeaderTab, minSup, set([]), myFreqList)
