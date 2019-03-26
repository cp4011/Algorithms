'''KD树构造和查找
Description
对给定的点集合构造KD树，要求如下：将方差最大的维度作为当前的分割维度，将数据集在分割维度上排序后的中位数作为分割点。程序要检索给定点对应的最近的K个点的坐标。
Input
输入第一行为测试用例个数，后面为测试用例，每一个用例包含三行，第一行为点集合（点之间用逗号隔开，两个坐标用空格隔开），第二行为检索的点，第三行为K值。
Output
输出每一个用例的最近K个点，按照距离从小到大的顺序打印。
Sample Input 1
1
3 5,6 2,5 8,9 3,8 6,1 1,2 9
8.2 4.6
2
Sample Output 1
8 6,9 3
'''
''' Kd-树 K-dimension tree是对数据点在k维空间（如二维(x，y)，三维(x，y，z)，k维(x，y，z..)）中划分的一种数据结构，
主要应用于多维空间关键数据的搜索（如：范围搜索和最近邻搜索）。基于欧式距离度量的,本质上说，Kd-树就是一种k-维平衡二叉树。
'''

# 暴力法（直接计算距离）
import math


def cal_dist(vect):
    return math.sqrt((vect[0][0] - vect[1][0]) ** 2 + (vect[0][1] - vect[1][1]) ** 2)
    # 错误 return math.sqrt((vect[0][0] - vect[0][1]) ** 2 + (vect[1][0] - vect[1][1]) ** 2)


num_case = int(input())
for _ in range(num_case):
    points = [(eval(i.split()[0]), eval(i.split()[1])) for i in input().split(",")]
    dest = tuple([eval(i) for i in input().split()])
    K = int(input())
    return_list = {}
    for point in points:
        return_list[point] = cal_dist((point, dest))
    sorted_return_list = sorted(return_list.items(), key=lambda x: x[1])
    res = ""
    for i in range(K):
        res += str(sorted_return_list[i][0][0]) + " " + str(sorted_return_list[i][0][1]) + ","
    print(res.rstrip(","))



