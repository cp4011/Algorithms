from numpy import *


def load_dataset():
    data_matrix = []
    label_matrix = []
    fr = open('testSet.txt')
    for line in fr.readlines():
        line_array = line.strip().split()
        data_matrix.append([1.0, float(line_array[0]), float(line_array[1])])       # 注意三个数要加上[]，里面的数要float()一下
        label_matrix.append(line_array[2])
    return data_matrix, label_matrix


def sigmoid(inX):
    return 1.0/(1+exp(-inX))


# （训练算法）1：梯度上升法
def grad_ascent(data_matrix_in, label_matrix):
    data_matrix = mat(data_matrix_in)           # 转化为numpy的矩阵，以便进行矩阵乘法
    label_matrix = mat(label_matrix).transpose()
    m, n = data_matrix.shape
    alpha = 0.001
    max_cycles = 500
    weights = ones((n, 1))
    for i in range(max_cycles):
        h = sigmoid(data_matrix * weights)                  # h和error是个n行的列向量
        error = label_matrix - h
        weights = weights + alpha * data_matrix.transpose() * error         # 记得转置
    return weights


# （训练算法）2.1 随机梯度上升法：stochastic gradient ascent
def stoc_grad_ascent0(data_matrix, class_labels):
    data_matrix = array(data_matrix)                       # 列表转化为numpy的数组，以便
    m, n = shape(data_matrix)
    weights = ones(n)
    alpha = 0.01
    for i in range(m):
        h = sigmoid(sum(data_matrix[i] * weights))          # h和error是个数值
        error = float(class_labels[i]) - float(h)
        weights = weights + alpha * data_matrix[i] * error
    return weights


# （训练算法）2.2 改进版随机梯度上升法
def stoc_grad_ascent1(data_matrix, class_labels, num_iter=150):
    data_matrix = array(data_matrix)          # 将列表如[1, 2, 3] 转换成numpy数组[1 2 3]  反过来转化成列表是：array([1,2,3]).tolist()
    m, n = shape(data_matrix)                 # 数组里是同类型的（如整数），内存连续。list里元素是地址的引用（一系列指针），内存不一定连续
    weights = ones(n)
    for i in range(num_iter):
        data_index = list(range(m))           # 为减少周期性波动，随机选取样本来更新参数。样本数据的索引。 返回的是range对象，list转换一下，60行才能索引删除
        for j in range(m):
            alpha = 4/(1.0+i+j) + 0.0001
            rand_index = int(random.uniform(0, len(data_index)))    # 随机产生索引 样本数据索引data_index 的下标
            h = sigmoid(sum(data_matrix[rand_index] * weights))     # 注意sum()
            error = class_labels[rand_index] - h
            weights = weights + alpha * data_matrix[rand_index] * error
            del(data_index[rand_index])       # 删除该样本数据索引，data_index中少一个数了，产生rand_index的范围也会小一个
    return weights


def classify_vector(inX, weights):
    prob = sigmoid(sum(inX * weights))      # 记住要sum()求和
    if prob > 0.5:
        return 1.0
    else:
        return 0.0


def colic_test():
    fr_train = open('horseColicTraining.txt')
    fr_test = open('horseColicTest.txt')
    training_set = []
    training_labels = []
    for line in fr_train.readlines():
        curr_line = line.strip().split('\t')
        line_array = [float(i) for i in curr_line]
        training_set.append(line_array[:-1])
        training_labels.append(line_array[-1])
    train_weights = stoc_grad_ascent1(training_set, training_labels, 1000)
    error_count = 0
    num_test_vector = 0
    for line in fr_test.readlines():
        num_test_vector += 1
        curr_line = line.strip().split('\t')
        line_array = [float(i) for i in curr_line]
        if classify_vector(line_array[:-1], train_weights) != line_array[-1]:
            error_count += 1
    error_rate = (float(error_count) / num_test_vector)
    print("the error rate of this test is: %f" % error_rate)
    return error_rate


def muti_test():
    num_tests = 10
    error_sum = 0.0
    for i in range(num_tests):
        error_sum += colic_test()
    print("After %d iterations, the average error rate is: %f" % (num_tests, error_sum / num_tests))
# 测试
# muti_test()


