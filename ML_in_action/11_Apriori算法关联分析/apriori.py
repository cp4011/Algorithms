from numpy import *


def loadDataSet():
    return [[1, 3, 4], [2, 3, 5], [1, 2, 3, 5], [2, 5]]


def createC1(dataset):
    '''
        构建初始候选项集的列表，即所有候选项集只包含一个元素，
        C1是大小为1的所有候选项集的集合
    '''
    C1 = []
    for transaction in dataset:
        for item in transaction:
            if [item] not in C1:
                C1.append([item])
    C1.sort()
    return list(map(frozenset, C1))   # rozenset"，是为了冻结集合，使集合由“可变”变为 "不可变"，这样，这些集合就可以作为字典的键值, list()


def scanD(dataset, Ck, min_support):
    '''
       计算Ck中的项集在数据集合D(记录或者transactions)中的支持度,
       返回满足最小支持度的项集的集合，和所有项集支持度信息的字典。
    '''
    ssCnt = {}
    for tid in dataset:
        for can in Ck:
            if can.issubset(tid):
                ssCnt[can] = ssCnt.get(can, 0) + 1
                # if not can in ssCnt:              # if not ssCnt.has_key(can): python3不支持
                #     ssCnt[can] = 1
                # else:
                #     ssCnt[can] += 1
    num_items = float(len(dataset))
    return_list = []
    support_data = {}
    for key in ssCnt:
        support = ssCnt[key] / num_items
        if support >= min_support:
            return_list.insert(0, key)
            # 错support_data[key] = support
        # 汇总支持度数据
        support_data[key] = support
    return return_list, support_data
# test
# dataset = loadDataSet()
# C1 = createC1(dataset)
# list, support = scanD(dataset, C1, 0.5)
# print(list)


def aprioriGen(Lk, k):
    retList = []
    lenLk = len(Lk)
    for i in range(lenLk):
        for j in range(i+1, lenLk):
            L1 = list(Lk[i])[:k-2]
            L2 = list(Lk[j])[:k-2]
            L1.sort()
            L2.sort()
            if L1 == L2:
                retList.append(Lk[i] | Lk[j])
    return retList


def apriori(dataset, minSupport = 0.5):
    C1 = createC1(dataset)
    D = list(map(set, dataset))
    L1, supportData = scanD(D, C1, minSupport)
    L = [L1]
    k = 2
    while (len(L[k-2]) > 0):
        Ck = aprioriGen(L[k-2], k)
        Lk, supK = scanD(D, Ck, minSupport)
        supportData.update(supK)    # dict.update(dict2)  dict2：添加到指定字典dict里的字典，有相同的键会直接替换成update的值
        L.append(Lk)
        k += 1
    return L, supportData
# test
# if __name__ == '__main__':
#     myDat = loadDataSet()
#     L, suppData = apriori(myDat, 0.5)
#     print(u"频繁项集L：", L)
#     print(u"所有候选项集的支持度信息：", suppData)


# 从频繁项集中挖掘关联规则

# 生成关联规则
def generateRules(L, supportData, minConf=0.7):
    # 频繁项集列表、包含那些频繁项集支持数据的字典、最小可信度阈值
    bigRuleList = []   # 存储所有的关联规则
    for i in range(1, len(L)):   # 只获取有两个或者更多集合的项目，从1,即第二个元素开始，L[0]是单个元素的
        # 两个及以上的才可能有关联一说，单个元素的项集不存在关联问题
        for freqSet in L[i]:
            H1 = [frozenset([item]) for item in freqSet]
            # 该函数遍历L中的每一个频繁项集并对每个频繁项集创建只包含单个元素集合的列表H1
            if (i > 1):
                # 如果频繁项集元素数目超过2,那么会考虑对它做进一步的合并
                rulesFromConseq(freqSet, H1, supportData, bigRuleList, minConf)
            else:   # 第一层时，后件数为1
                calcConf(freqSet, H1, supportData, bigRuleList, minConf)    # 调用函数2
    return bigRuleList


# 生成候选规则集合：计算规则的可信度以及找到满足最小可信度要求的规则
def calcConf(freqSet, H, supportData, brl, minConf=0.7):
    # 针对项集中只有两个元素时，计算可信度
    prunedH = []    # 返回一个满足最小可信度要求的规则列表
    for conseq in H:    # 后件，遍历 H中的所有项集并计算它们的可信度值
        conf = supportData[freqSet]/supportData[freqSet-conseq] # 可信度计算，结合支持度数据
        if conf >= minConf:
            print (freqSet-conseq, '-->', conseq, 'conf:', conf)
            # 如果某条规则满足最小可信度值,那么将这些规则输出到屏幕显示
            brl.append((freqSet-conseq, conseq, conf))  # 添加到规则里，brl 是前面通过检查的 bigRuleList
            prunedH.append(conseq)  # 同样需要放入列表到后面检查
    return prunedH


#合并
def rulesFromConseq(freqSet, H, supportData, brl, minConf=0.7):
    # 参数:一个是频繁项集,另一个是可以出现在规则右部的元素列表 H
    m = len(H[0])
    if (len(freqSet) > (m + 1)):    # 频繁项集元素数目大于单个集合的元素数
        Hmp1 = aprioriGen(H, m+1)   # 存在不同顺序、元素相同的集合，合并具有相同部分的集合
        Hmp1 = calcConf(freqSet, Hmp1, supportData, brl, minConf)   # 计算可信度
        if (len(Hmp1) > 1):
            # 满足最小可信度要求的规则列表多于1,则递归来判断是否可以进一步组合这些规则
            rulesFromConseq(freqSet, Hmp1, supportData, brl, minConf)

# test
# if __name__ == '__main__':
#     myDat = loadDataSet()
#     L, suppData = apriori(myDat, 0.5)
#     rules = generateRules(L, suppData, minConf=0.7)
#     print('rules:\n', rules)






