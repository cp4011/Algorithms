from numpy import *


def load_dataset():                                 # 加载数据集
    data_matrix = []
    label_matrix = []
    fr = open('testSet.txt')                        # testSet.txt：数据集
    for line in fr.readlines():
        line_array = line.strip().split()
        data_matrix.append([1.0, float(line_array[0]), float(line_array[1])])  # 注意三个数要加上[]，里面的数要float()一下
        label_matrix.append(line_array[2])
    return data_matrix, label_matrix                # data_matrix：数据矩阵100*3, label_matrix：类别标签矩阵1*100


def sigmoid(inX):                                   # sigmoid函数: 1.0/(1+exp(-s))
    return 1.0/(1+exp(-inX))


"""梯度上升法法伪代码
每个回归系数初始化为1
重复R次：
    计算整个数据集的梯度
    使用alpha 下gradient 更新回归系数的向量
返回回归系数
"""


# （训练算法）1：梯度上升法
def grad_ascent(data_matrix_in, label_matrix):      # data_matrix_in：数据矩阵100*3, label_matrix：类别标签矩阵1*100
    data_matrix = mat(data_matrix_in)               # 转换为numpy的矩阵，以便进行矩阵乘法
    label_matrix = mat(label_matrix).transpose()    # 转换为numpy矩阵并转置为labelMat：100*1
    m, n = data_matrix.shape                        # 获得矩阵行列数
    alpha = 0.001                                   # 初始化移动步长
    max_cycles = 500                                # #初始化迭带次数
    weights = ones((n, 1))                          # 初始化权重参数矩阵，初始值都为1
    for i in range(max_cycles):                     # 开始迭代计算参数
        h = sigmoid(data_matrix * weights)          # h和error是个n行的列向量，100*3 * 3*1 => 100*1
        error = label_matrix - h                    # 计算误差100*1
        # error = label_matrix.astype('float64') - h.astype('float64') # numpy中.astype('float64')类型转换，不写画图时会报错
        weights = weights + alpha * data_matrix.transpose() * error    # 更新参数值，记得转置
    return weights                                  # 返回权重参数矩阵


"""随机梯度上升法伪代码：
所有回归系数初始化为1
对数据集中每个样本
    计算该样本的梯度
    使用alpha x gradient 更新回归系数值
返回回归系数值
随机梯度上升算法与梯度上升算法在代码上很相似，但也有一些区别：1.后者的变量h和误差error都是向量，而前者则全是数值；
2.前者没有矩阵的转换过程，所有变量的数据类型都是Numpy数组
"""


# （训练算法）2.1 随机梯度上升法：stochastic gradient ascent
def stoc_grad_ascent0(data_matrix, class_labels):           # data_matrix_in：数据矩阵100*3, label_matrix：类别标签矩阵1*100
    data_matrix = array(data_matrix)                        # 列表转化为numpy的数组，以便
    m, n = shape(data_matrix)                               # 获取数据列表大小
    weights = ones(n)                                       # 初始化权重参数矩阵，初始值都为1
    alpha = 0.01
    for i in range(m):                                      # 遍历每一行数据
        h = sigmoid(sum(data_matrix[i] * weights))          # h和error是个数值  1*3 * 3*1
        error = class_labels[i] - h                         # 计算误差
        weights = weights + alpha * data_matrix[i] * error  # 更新权重值
    return weights                                          # 返回权重参数矩阵


# （训练算法）2.2 改进版随机梯度上升法
def stoc_grad_ascent1(data_matrix, class_labels, num_iter=150):  # data_matrix_in：数据矩阵100*3, label_matrix：类别标签矩阵1*100
    data_matrix = array(data_matrix)          # 将列表如[1, 2, 3] 转换成numpy数组[1 2 3]  反过来转化成列表是：array([1,2,3]).tolist()
    m, n = shape(data_matrix)                 # 数组里是同类型的（如整数），内存连续。list里元素是地址的引用（一系列指针），内存不一定连续
    weights = ones(n)
    for i in range(num_iter):                 # 开始迭代，迭代次数为numIter
        data_index = list(range(m))           # 为减少周期性波动，随机选取样本来更新参数。样本数据的索引。返回的是range对象，需list转换一下
        for j in range(m):
            alpha = 4/(1.0+i+j) + 0.0001
            rand_index = int(random.uniform(0, len(data_index)))    # 随机产生索引 样本数据索引data_index 的下标，从而减少随机性的波动
            h = sigmoid(sum(data_matrix[rand_index] * weights))     # 序列号对应的元素与权重矩阵相乘，求和后再求sigmoid。注意sum()
            error = class_labels[rand_index] - h                    # 求误差
            weights = weights + alpha * data_matrix[rand_index] * error     # 更新权重矩阵
            del(data_index[rand_index])         # 删除该样本数据索引，data_index中少一个数了，产生rand_index的范围也会小一个
    return weights                              # 返回权重参数矩阵


def classify_vector(inX, weights):          # 分类函数  inX：计算得出的矩阵100*1，weights：权重参数矩阵
    prob = sigmoid(sum(inX * weights))      # #计算sigmoid值   记住要sum()求和
    if prob > 0.5:                          # 返回分类结果
        return 1.0
    else:
        return 0.0


def colic_test():                               # 训练和测试函数
    fr_train = open('horseColicTraining.txt')   # 打开训练集
    fr_test = open('horseColicTest.txt')
    training_set = []                           # 初始化训练集数据列表
    training_labels = []
    for line in fr_train.readlines():           # 遍历训练集数据
        curr_line = line.strip().split('\t')    # 切分数据集
        line_array = [float(i) for i in curr_line]
        training_set.append(line_array[:-1])
        training_labels.append(line_array[-1])
    train_weights = stoc_grad_ascent1(training_set, training_labels, 1000)      # 获得权重参数矩阵
    error_count = 0
    num_test_vector = 0
    for line in fr_test.readlines():                # 遍历测试集数据
        num_test_vector += 1
        curr_line = line.strip().split('\t')
        line_array = [float(i) for i in curr_line]
        if classify_vector(line_array[:-1], train_weights) != line_array[-1]:   # 如果分类结果和分类标签不符，则错误计数+1
            error_count += 1
    error_rate = (float(error_count) / num_test_vector)         # 计算分类错误率
    print("the error rate of this test is: %f" % error_rate)
    return error_rate                                           # 返回分类错误率


def muti_test():                    # 求均值函数
    num_tests = 10                  # 迭代次数
    error_sum = 0.0                 # 初始错误率和
    for i in range(num_tests):      # 调用十次colicTest()，累加错误率
        error_sum += colic_test()
    print("After %d iterations, the average error rate is: %f" % (num_tests, error_sum / num_tests))    # 打印平均分类结果
# 测试
muti_test()

