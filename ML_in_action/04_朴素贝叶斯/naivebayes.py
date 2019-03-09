from numpy import *


def load_dataset():
    posting_list = [['my', 'dog', 'has', 'flea', 'problems', 'help', 'please'],     # 词条切分后的文档集合
                 ['maybe', 'not', 'take', 'him', 'to', 'dog', 'park', 'stupid'],
                 ['my', 'dalmation', 'is', 'so', 'cute', 'I', 'love', 'him'],
                 ['stop', 'posting', 'stupid', 'worthless', 'garbage'],
                 ['mr', 'licks', 'ate', 'my', 'steak', 'how', 'to', 'stop', 'him'],
                 ['quit', 'buying', 'worthless', 'dog', 'food', 'stupid']]
    class_vector = [0, 1, 0, 1, 0, 1]           # 类别标签的集合，1 is abusive（辱骂）, 0 not
    return posting_list, class_vector           # 词条切分后的文档集合和类别标签集合


def create_vocab_list(dataset):             # 创建一个包含所有文档中出现的不重复词的列表
    vocabulary_set = set([])                # 空集合set()
    for document in dataset:                # 将新词集合添加到创建的集合中
        vocabulary_set = vocabulary_set | set(document)     # 操作符 | 用于求两个集合的并集
    return list(vocabulary_set)             # 返回一个包含所有文档中出现的不重复词的列表


# 准备数据（两种实现方式：词集模型，词袋模型）
# 1. (基于贝努利模型实现的朴素贝叶斯)  ***词的出现与否，词集模型（set-of-words model)***
def set_of_words2vec(vocab_list, input_set):                # vocabList:词汇表，inputSet:某个文档
    return_vector = [0] * len(vocab_list)                   # 创建一个所含元素都为0的向量
    for word in input_set:
        if word in vocab_list:
            return_vector[vocab_list.index(word)] = 1       # 只考虑词是否在文档中出现，不考虑次数
        else:
            print("the word: %s is not in my Vocabulary!" % word)
    return return_vector                                    # 向量的每一个元素为1或0，表示词汇表中的单词在文档中是否出现


# 2. (基于多项式模型实现的朴素贝叶斯)  ***朴素贝叶斯词袋模型（bag-of-words model)***
def bag_of_words2vec(vocab_list, input_set):                #
    return_vector = [0] * len(vocab_list)
    for word in input_set:
        if word in vocab_list:
            return_vector[vocab_list.index(word)] += 1
        return return_vector


def train_naivebayes(train_matrix, train_category):
    """
       Function：   朴素贝叶斯分类器训练函数
       Args：       trainMatrix：文档矩阵
                   trainCategory：类别标签向量
       Returns：   pos0_vector：非侮辱性词汇概率向量
                   pos1_vector：侮辱性词汇概率向量
                   pos_abusive：侮辱性文档概率
    """
    num_train_documents = len(train_matrix)                         # 获得训练集中文档个数
    num_words = len(train_matrix[0])                                # 获得训练集中单词个数
    pos_abusive = sum(train_category) / float(len(train_category))  # 计算文档属于侮辱性文档的概率
    pos0_num = ones(num_words)                                      # 初始化概率的分子变量 zeros() change to ones()
    pos1_num = ones(num_words)                                      # 防止一个概率值为0，最后的乘积也为0
    pos0_denom = 2.0                            # 初始化概率的分母变量 0.0 change to 2.0
    pos1_denom = 2.0                            # 乘积取自然对数，避免下溢或浮点数舍入导致的错误,取值虽然不同，但是不影响最终结果
    for i in range(num_train_documents):        # 遍历训练集trainMatrix中所有文档
        if train_category[i] == 1:              # 如果侮辱性词汇出现，则侮辱词汇计数加一，且文档的总词数加一
            pos1_num += train_matrix[i]         # 数组（相加）
            pos1_denom += sum(train_matrix[i])  # 数字
        else:                                   # 如果非侮辱性词汇出现，则非侮辱词汇计数加一，且文档的总词数加一
            pos0_num += train_matrix[i]         # 数组
            pos0_denom += sum(train_matrix[i])  # 数字
    # pos1_vector = pos1_num / float(pos1_denom)  # 对每个元素做除法求概率
    # pos0_vector = pos0_num / float(pos0_denom)
    pos1_vector = log(pos1_num / float(pos1_denom))  # 改进版：等式两边取自然对数ln(a*b)=lna+lnb（防止下溢出：太多小数相乘四舍五入变成0）
    pos0_vector = log(pos0_num / float(pos0_denom))
    return pos0_vector, pos1_vector, pos_abusive     # 返回两个类别概率向量和一个概率


def classifyNB(vec2classify, pos0_vector, pos1_vector, pos_abusive):
    """
      Function：   朴素贝叶斯分类函数                     求：P(Ci|X) = P(X|Ci)*P(Ci)  /  P(X)          两边取对数ln
      Args：       vec2Classify：文档矩阵                     X
                  pos0_vector：非侮辱性词汇概率向量        P(Xi|C0)
                  pos1_vector：侮辱性词汇概率向量          P(Xi|C1)
                  pos_abusive：侮辱性文档概率              P(C1)       P(C0) = 1 - P(C1)
      Returns：    1：侮辱性文档
                  0：非侮辱性文档
    """
    p1 = sum(vec2classify * pos1_vector) + log(pos_abusive)   # 向量元素相乘后求和再加到类别的对数概率上，等价于概率相乘
    p0 = sum(vec2classify * pos0_vector) + log(1.0-pos_abusive)
    if p1 > p0:
        return 1        # 侮辱性文档
    else:
        return 0        # 非侮辱性文档


# 朴素贝叶斯分类器测试函数，可以使用词集/词袋模型，此处使用的是词集函数set_of_words2vec()
def testingNB():                                            # 便利函数（封装了之前的所有操作）
    list_posts, list_classes = load_dataset()
    my_vocab_list = create_vocab_list(list_posts)           # 构建一个包含所有词的列表
    train_matrix = []                                       # 初始化训练数据列表
    for post_in_document in list_posts:                     # 填充训练数据列表
        train_matrix.append(set_of_words2vec(my_vocab_list, post_in_document))
    pos0_vector, pos1_vector, pos_abusive = train_naivebayes(train_matrix, list_classes)    # 训练
    test_entry = ['love', 'my', 'dalmation']                                                # 测试
    this_document = set_of_words2vec(my_vocab_list, test_entry)
    print(test_entry, "classified as: %d" % classifyNB(this_document, pos0_vector, pos1_vector, pos_abusive))
    test_entry = ['stupid', 'garbage']                                                      # 测试
    this_document = set_of_words2vec(my_vocab_list, test_entry)
    print(test_entry, "classified as: %d" % classifyNB(this_document, pos0_vector, pos1_vector, pos_abusive))
# 测试
# testingNB()


# 垃圾邮件测试
def text_parser(big_string):        # 切分文本,接受一个大写字符串并将其解析为字符串列表,bigString：输入字符串
    import re
    list_of_tokens = re.split(r'\W*', big_string)   # 利用正则表达式来切分句子，其中分隔符是除单词、数字外的任意字符串
    return [tok.lower() for tok in list_of_tokens if len(tok) > 2]  # 返回切分后的字符串列表,将字符串全部转换成小写.lower()或者大写.upper()


# 贝叶斯垃圾邮件分类器
def spam_test():                    # 可以使用词集/词袋模型，此处使用的是词袋函数bag_of_words2vec()
    doc_list = []
    class_list = []
    full_text = []                  # 在此函数没有用，以后可能会用到，可以作为返回值return出去
    for i in range(1, 26):          # 导入文本文件
        word_list = text_parser(open('email/spam/%d.txt' % i).read())       # 打开并解析垃圾邮件
        doc_list.append(word_list)          # 切分后的文本以原始列表形式加入文档列表
        class_list.append(1)                # 标签列表更新
        full_text.extend(word_list)         # 切分后的文本直接合并到词汇列表
        word_list = text_parser(open('email/ham/%d.txt' % i).read())
        doc_list.append(word_list)
        class_list.append(0)
        full_text.extend(word_list)

    vocab_list = create_vocab_list(doc_list)             # 创建一个包含所有文档中出现的不重复词的列表
    training_set = list(range(50))                       # doc_list中训练集文档的索引 python3.x:range返回range对象,list()转化
    test_set = []               # doc_list中测试集的索引 采用留存交叉验证法，50个邮件文档中随机选择10个留存作为测试集,并从训练样本中剔除
    for i in range(10):
        rand_index = int(random.uniform(0, len(training_set)))  # 随机从0到测试集还剩索引的个数之间选取一个数字作为training_set的index索引
        test_set.append(training_set[rand_index])        # 将该样本所属的索引加入测试集中
        del(training_set[rand_index])         # 将该样本从训练集中剔除,删除训练集中的第rand_index个位置的索引，该索引上存储着可以直接访问doc_list的索引下标
    train_matrix = []                         # 初始化训练集数据列表和标签列表
    train_classes = []
    for i in training_set:                               # 遍历训练集 train the classifier (get probs)
        train_matrix.append(bag_of_words2vec(vocab_list, doc_list[i]))  # 词表转换到向量，并加入到训练数据列表中
        train_classes.append(class_list[i])              # 相应的标签也加入训练标签列表中
    pos0_vector, pos1_vector, pos_abusive = train_naivebayes(train_matrix, train_classes)   # 朴素贝叶斯分类器训练函数
    err_count = 0                                        # 初始化错误计数
    for i in test_set:                                   # 遍历测试集进行测试
        word_vector = bag_of_words2vec(vocab_list, doc_list[i])    # 词表转换到向量，注意要转成词向量才能作为参数传入函数中
        if classifyNB(word_vector, pos0_vector, pos1_vector, pos_abusive) != class_list[i]:  # 判断分类结果与原标签是否一致
            err_count += 1                               # 如果不一致则错误计数加1
            print("classification error is:", doc_list[i])
    print("the error counts is:", err_count)
    print("the error rate is: %f" % (float(err_count) / len(test_set)))
    return vocab_list, full_text                         # 返回词汇表和全部单词列表(此处的返回值可以用于下一个应用)
# 测试
# spam_test()                                            # 结果有随机性，因为采用留存交叉验证，随机选择测试集


# 使用朴素贝叶斯分类器从个人广告中获取区域倾向（并未亲自实现，拷贝）
def calcMostFreq(vocabList, fullText):
    """
        Function：   计算出现频率
        Args：       vocabList：词汇表
                    fullText：全部词汇
        Returns：    sortedFreq[:30]：出现频率最高的30个词
    """
    import operator
    freqDict = {}
    for token in vocabList:
        freqDict[token] = fullText.count(token)
    sortedFreq = sorted(freqDict.items(), key=operator.itemgetter(1), reverse=True)
    return sortedFreq[:30]


def localWords(feed1, feed0):
    """
        Function：   RSS源分类器
        Args：       feed1：RSS源
                    feed0：RSS源          RSS(Really Simple Syndication,简易信息聚合)
        Returns：    vocabList：词汇表
                    p0V：类别概率向量
                    p1V：类别概率向量
    """
    import feedparser   # Python的Feed解析库,可以处理RSS ，CDF，Atom 使用它可从任何RSS或Atom订阅源得到标题、链接和文章的条目
    # 初始化数据列表
    docList = []; classList = []; fullText = []
    minLen = min(len(feed1['entries']), len(feed0['entries']))
    # 导入文本文件
    for i in range(minLen):
        # 切分文本
        wordList = text_parser(feed1['entries'][i]['summary'])
        # 切分后的文本以原始列表形式加入文档列表
        docList.append(wordList)
        # 切分后的文本直接合并到词汇列表
        fullText.extend(wordList)
        # 标签列表更新
        classList.append(1)
        # 切分文本
        wordList = text_parser(feed0['entries'][i]['summary'])
        # 切分后的文本以原始列表形式加入文档列表
        docList.append(wordList)
        # 切分后的文本直接合并到词汇列表
        fullText.extend(wordList)
        # 标签列表更新
        classList.append(0)
    # 获得词汇表
    vocabList = create_vocab_list(docList)
    # 获得30个频率最高的词汇
    top30Words = calcMostFreq(vocabList, fullText)
    # 去掉出现次数最高的那些词
    for pairW in top30Words:
        if pairW[0] in vocabList: vocabList.remove(pairW[0])
    trainingSet = range(2*minLen); testSet = []
    # 随机构建测试集，随机选取二十个样本作为测试样本，并从训练样本中剔除
    for i in range(20):
        # 随机得到Index
        randIndex = int(random.uniform(0, len(trainingSet)))
        # 将该样本加入测试集中
        testSet.append(trainingSet[randIndex])
        # 同时将该样本从训练集中剔除
        del(trainingSet[randIndex])
    # 初始化训练集数据列表和标签列表
    trainMat = []; trainClasses = []
    # 遍历训练集
    for docIndex in trainingSet:
        # 词表转换到向量，并加入到训练数据列表中
        trainMat.append(set_of_words2vec(vocabList, docList[docIndex]))
        # 相应的标签也加入训练标签列表中
        trainClasses.append(classList[docIndex])
    # 朴素贝叶斯分类器训练函数
    p0V, p1V, pSpam = train_naivebayes(array(trainMat), array(trainClasses))
    # 初始化错误计数
    errorCount = 0
    # 遍历测试集进行测试
    for docIndex in testSet:
        # 词表转换到向量
        wordVector = set_of_words2vec(vocabList, docList[docIndex])
        # 判断分类结果与原标签是否一致
        if classifyNB(array(wordVector), p0V, p1V, pSpam) != classList[docIndex]:
            # 如果不一致则错误计数加1
            errorCount += 1
            # 并且输出出错的文档
            print("classification error",docList[docIndex])
    # 打印输出信息
    print('the erroe rate is: ', float(errorCount)/len(testSet))
    # 返回词汇表和两个类别概率向量
    return vocabList, p0V, p1V


def getTopWords(ny, sf):
    """
        Function：   最具表征性的词汇显示函数
        Args：       ny：RSS源
                    sf：RSS源
        Returns：    打印信息
    """
    import operator
    # RSS源分类器返回概率
    vocabList, p0V, p1V=localWords(ny, sf)
    # 初始化列表
    topNY = []; topSF = []
    # 设定阈值，返回大于阈值的所有词，如果输出信息很多，就提高一下阈值
    for i in range(len(p0V)):
        if p0V[i] > -4.5 : topSF.append((vocabList[i], p0V[i]))
        if p1V[i] > -4.5 : topNY.append((vocabList[i], p1V[i]))
    # 排序
    sortedSF = sorted(topSF, key=lambda pair: pair[1], reverse=True)
    print("SF**SF**SF**SF**SF**SF**SF**SF**SF**SF**SF**SF**SF**SF**SF**SF**")
    # 打印
    for item in sortedSF:
        print(item[0])
    # 排序
    sortedNY = sorted(topNY, key=lambda pair: pair[1], reverse=True)
    print("NY**NY**NY**NY**NY**NY**NY**NY**NY**NY**NY**NY**NY**NY**NY**NY**")
    # 打印
    for item in sortedNY:
        print(item[0])
#test
# ny = feedparser.parse('http://newyork.craiglist.org/stp/index.rss')
# sf = feedparser.parse('http://sfbay.craiglist.org/stp/index.rss')
# vocabList, pSF, pNY = localWords(ny, sf)
# getTopWords(ny, sf)
