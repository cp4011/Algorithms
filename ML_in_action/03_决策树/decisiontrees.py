from math import log

"""决策树
优点：计算复杂度不高，输出结果易于理解，对中间值的缺失不敏感，可以处理不相关特征数据。
缺点：可能会产生过度匹配问题。
适用数据类型：数值型和标称型。

递归构建决策树:
递归结束的条件：程序遍历完所有划分数据集的属性，或者每个分支下的所有实例都具有相同的分类。如果所欲实例都具有相同的分类，
则得到一个叶子节点或者终止块。任何到达叶子节点的数据必须属于叶子节点的分类
"""


def create_dataset():
    dataset = [[1, 1, 'yes'],
               [1, 1, 'yes'],
               [1, 0, 'no'],
               [0, 1, 'no'],
               [0, 1, 'no']]
    # 分清: 特征feature 和 类别class
    labels = ['no surfacing', 'flippers']       # dataset中第一、二列的特征标签向量feature_labels
    return dataset, labels


# 计算信息熵
def clac_shannon_entropy(dataset):
    length = len(dataset)                       # 计算数据集中实例的总数
    dict = {}
    for line in dataset:
        label = line[-1]
        if label not in dict.keys():
            dict[label] = 0
        dict[label] += 1
    entropy = 0.0
    for key in dict.keys():                      # 利用所有类别标签发生频率计算类别出现的概率
        pro = float(dict[key]) / length          # pro = dict[key] / length
        entropy -= pro * log(pro, 2)
    return entropy                               # 返回香农熵计算结果
# 测试
# dataset, labels = create_dataset()
# print(clac_shannon_entropy(dataset))


def split_dataset(dataset, axis, value):
    """
       Function：   按照给定特征划分数据集
       Args：       dataSet：带划分的数据集
                   axis：划分数据集的特征
                   value：需要返回的特征的值
       Returns：    retDataSet：符合特征的数据集
    """
    result = []
    for line in dataset:
        if line[axis] == value:                 # 将符合特征的数据抽取出来
            line_result = line[0:axis]          # 截取列表中第axis-1个之前的数据
            line_result.extend(line[axis+1:])   # 将第axis+1之后的数据接入到上述数据集
            result.append(line_result)          # 将处理结果作为列表接入到返回数据集
    return result                               # 返回符合特征的数据集
#测试
# dataset, labels = create_dataset()
# print(split_dataset(dataset, 0, 1))


def choose_best_feature_to_split(dataset):
    length = len(dataset[0]) - 1                    # 初始化特征数量
    base_entropy = clac_shannon_entropy(dataset)    # 计算原始香农熵
    best_info_gain = 0.0                            # 初始化信息增益和最佳特征
    best_feature = -1
    for i in range(length):                         # 选出最好的划分数据集的特征
        feat_list = [example[i] for example in dataset]      # 创建唯一的分类标签列表
        feat_list = set(feat_list)                           # 从列表中创建集合，以得到列表中唯一元素值
        entropy = 0.0
        for j in feat_list:                                     # 计算每种划分方式的信息熵
            sub_dataset = split_dataset(dataset, i, j)
            pro = float(len(sub_dataset)) / float(len(dataset))
            entropy += pro * clac_shannon_entropy(sub_dataset)  # 这里不是-=
        info_gain = base_entropy - entropy                      # 得到信息增益
        if info_gain > best_info_gain:
            best_info_gain = info_gain
            best_feature = i
    return best_feature                                     # 返回划分数据集最好的特征
# 测试
# dataset, labels = create_dataset()
# print(choose_best_feature_to_split(dataset))


"""如果数据集已经处理了所有的属性，但是类标签依然不是唯一的，此时我们需要决定如何定义该叶子节点，在这种情况下，
采用的是多数表决的方法决定该叶子节点的分类。"""


# 多数表决法（决定该叶子节点的分类）
def majority_count(class_list):     # classList：分类列表
    dict = {}
    for i in class_list:            # 给字典赋值
        if i not in dict.keys():    # 如果字典中没有该键值，则创建
            dict[i] = 0
        dict[i] += 1
    result = sorted(dict.items(), key=lambda x: x[1], reverse=True)     # 排序
    return result[0][0]             # 返回叶子结点分类结果


# 构建决策树
def create_tree(dataset, labels):
    class_list = [example[-1] for example in dataset]       # 创建分类列表
    if class_list.count(class_list[0]) == len(class_list):  # 类别完全相同则停止划分
        return class_list[0]
    if len(dataset[0]) == 1:                                # 遍历完所有特征时返回出现次数最多的类别
        return majority_count(class_list)                   # 此处参数必须是列表class_list，dataset作为参数的话可能是[['no']]
    best_feature = choose_best_feature_to_split(dataset)    # 选取最好的分类特征
    best_feature_label = labels[best_feature]
    del(labels[best_feature])
    my_tree = {best_feature_label: {}}                      # 创建字典存储树的信息
    feature_value = [example[best_feature] for example in dataset]   # 得到列表包含的所有属性值
    feature_value = set(feature_value)                      # 从列表中创建集合
    for value in feature_value:                             # 遍历当前选择特征包含的所有属性值
        sub_labels = labels.copy()   # 复制类标签列表，避免树搞错存在的标签 必须加上list.copy()或者a[:]。Python中函数参数是列表时，参数是按照引用传递的
        # 递归调用函数createTree()，返回值将被插入到字典变量myTree中
        my_tree[best_feature_label][value] = create_tree(split_dataset(dataset, best_feature, value), sub_labels)
    return my_tree                                      # 返回字典变量myTree
# 测试
# dataset, labels = create_dataset()
# print(create_tree(dataset, labels))
# 构建树结果: {'no surfacing': {0: 'no', 1: {'flippers': {0: 'no', 1: 'yes'}}}}
"""变量myTree包含了很多代表树结构信息的嵌套字典，从左边开始，第一个关键字no surfacing是第一个划分数据集的特征名称，
该关键字的值也是另一个数据字典。第二个关键字是no surfacing特征划分的数据集，这些关键字的值是no surfacing节点的子节点。
这些值可能是类标签，也可能是另一个数据字典，如果值是标签，则该子节点是叶子结点；如果是另一个数据字典，则子节点是一个
判断节点，这种格式结构不断重复就构成了整棵树。
"""


# 使用决策树进行分类
def classify(input_tree, feature_label, test_vector):   # inputTree:树信息; featLabels:标签列表; testVec:测试数据
    # 第一个关键字为第一次划分数据集的类别标签，附带的取值表示子节点的取值
    first_str = list(input_tree.keys())[0]              # 将返回的对象明确转化成list，因此支持indexable
    second_dict = input_tree[first_str]                 # 新的树，相当于脱了一层皮
    index = feature_label.index(first_str)              # 将标签字符串转为索引
    value = test_vector[index]                          # 取测试数据中第一次划分数据集的类别标签的特征值
    find_result = second_dict[value]
    result = find_result
    if isinstance(find_result, dict):                   # 判断子节点是否为字典类型，进而得知是否到达叶子结点
        result = classify(find_result, feature_label, test_vector)  # 没到达叶子结点，则递归调用classify()
    return result                                       # 到达叶子结点，则分类结果为当前节点的分类标签,返回分类标签
# 测试
# dataset, labels = create_dataset()
# import copy
# # labels_ = labels                                出错 直接赋值: 默认浅拷贝传递对象的引用而已,原始列表改变，被赋值的 也会做相同的改变
# labels_ = copy.deepcopy(labels)                 # 深复制labels，因为create_tree()会将labels列表中的元素删掉
# print(classify(create_tree(dataset, labels), labels_, [1, 1]))


def store_tree(input_tree, filename):
    import pickle
    # fw = open(filename, 'wb')                  # 注意wb要加上 引号，加上b
    # pickle.dump(input_tree, fw)
    # fw.close()                                 # 记得close()
    with open(filename, 'wb') as fw:
        pickle.dump(input_tree, fw)


def load_tree(filename):
    import pickle
    fr = open(filename, 'rb')                    # 默认为只读，'r'可不写，注意加上b
    return pickle.load(fr)                       # 返回树信息


# 使用决策树预测隐形眼镜类型(软、硬材质、不适合佩戴）
import treePlotter
def main():
    fr = open('lenses.txt')                                                  # 打开文件
    lenses = [inst.strip().split('\t') for inst in fr.readlines()]           # 读取文件信息
    lensesLabels = ['age', 'prescript', 'astigmatic', 'tearRate']            # 定义标签
    lensesTree = create_tree(lenses, lensesLabels)                           # 创建树
    print(lensesTree)                                                        # 打印树信息
    treePlotter.createPlot(lensesTree)                                       # 绘制树信息


#测试
if __name__ == '__main__':
    # dataset, labels = create_dataset()
    # my_tree = create_tree(dataset, labels)
    # store_tree(my_tree, 'tree_storage.txt')          # 注意文件名要加上 引号
    # print(load_tree('tree_storage.txt'))
    main()

