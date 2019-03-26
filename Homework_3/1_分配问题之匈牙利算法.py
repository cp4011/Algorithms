'''分配问题之匈牙利算法
Description
对给定的n个任务与n个人之间的成本矩阵完成成本最低的任务分配策略。使用匈牙利算法完成。
Input
输入：第一行为用例个数，之后为每一个用例；用例的第一行为任务个数，即n；用例的第二行为使用逗号隔开的人员完成任务的成本；
每一个成本描述包括人员序号、任务序号和成本，使用空格隔开。人员序号和任务序号都是从1到n的整数，序号出现的次序没有固定规则。
Output
输出：每一个用例输出一行，从序号为1的人员开始，给出其分配的任务序号，使用空格隔开；使用逗号将多个解隔开。
Sample Input 1
1
4
2 1 6,1 2 2,1 3 7,1 4 8,1 1 9,2 2 4,2 3 3,2 4 7,3 1 5,3 2 8,3 3 1,3 4 8,4 1 7,4 2 6,4 3 9,4 4 4
Sample Output 1
2 1 3 4
'''
'''
列：人员序号1-4；  行：任务序号1-4； 值：成本
例子中cost开销矩阵：    9 2 7 8
                        6 4 3 7
                        5 8 1 8
                        7 6 9 4
'''

candidates = []

# （     也可使用 import itertools   全排列：candidates = list(itertools.permutations([1, 2, 3, 4], 4))
#  组合：candidates = list(itertools.combinations('abc', 2))    )
# 自定义的全排列
def permutations(arr, position, end):
    global candidates
    if position == end:
        list1 = [0] * len(arr)
        for i in range(len(arr)):
            list1[i] = arr[i]
        candidates.append(list1)
    else:
        for index in range(position, end):
            arr[index], arr[position] = arr[position], arr[index]
            permutations(arr, position + 1, end)
            arr[index], arr[position] = arr[position], arr[index]


t = int(input())
for i in range(t):
    n = int(input())
    arr = [i + 1 for i in range(n)]

    dictionary = {}     # 用字典存储 开销矩阵
    candidates = []
    permutations(arr, 0, len(arr))

    rawdata = input().split(',')
    for item in rawdata:
        data = [int(i) for i in item.split(' ')]
        cur_key = (data[0], data[1])    # 使得字典的键key为 元组tuple
        cur_value = data[2]
        dictionary[cur_key] = cur_value

    min_cost = 10000000000

    for candidate in candidates:    # candidates = [(1, 2, 3, 4), (1, 2, 4, 3), (1, 3, 2, 4), ...] 共24中排列
        cost = 0
        for i in range(len(arr)):
            cost += dictionary[(arr[i], candidate[i])]      # *************计算全排列的每一次开销（精髓）************
                                                            # 其实 arr[i] 可以用 i+1 代替
        if min_cost > cost:         # 记住最小的开销
            min_cost = cost

    result_set = []
    for candidate in candidates:
        cost = 0
        for i in range(len(arr)):
            cost += dictionary[(arr[i], candidate[i])]
        if cost == min_cost:                # 可能存在多个解
            result_set.append(candidate)

    for i in range(len(arr) - 1, -1, -1):
        result_set.sort(key=lambda x: x[i], reverse=True)       # 多个解的 输出排序顺序

    res_str = ''
    for result in result_set:
        for index in range(n):
            res_str += str(result[index]) + ' '
        res_str = res_str[:-1]      # 去掉最后一个 空格
        res_str += ','
    res_str = res_str[:-1]          # 去掉最后一个 逗号
    print(res_str)




# import itertools
# import numpy as np
# from numpy import random
# from scipy.optimize import linear_sum_assignment
#
#
# # 任务分配类
# class TaskAssignment:
#
#     # 类初始化，需要输入参数有任务矩阵以及分配方式，其中分配方式有两种，全排列方法all_permutation或匈牙利方法Hungary。
#     def __init__(self, task_matrix, mode):
#         self.task_matrix = task_matrix
#         self.mode = mode
#         if mode == 'all_permutation':
#             self.min_cost, self.best_solution = self.all_permutation(task_matrix)
#         if mode == 'Hungary':
#             self.min_cost, self.best_solution = self.Hungary(task_matrix)
#
#     # 全排列方法
#     ''' for item in itertools.permutations(['a', 'b', 'c']):
#             print item
#         ('a', 'b', 'c')
#         ('a', 'c', 'b')
#         ('b', 'a', 'c')
#         ('b', 'c', 'a')
#         ('c', 'a', 'b')
#         ('c', 'b', 'a')
# '''
#     def all_permutation(self, task_matrix):
#         number_of_choice = len(task_matrix)
#         solutions = []
#         values = []
#         for each_solution in itertools.permutations(range(number_of_choice)):
#             each_solution = list(each_solution)
#             solution = []
#             value = 0
#             for i in range(len(task_matrix)):
#                 value += task_matrix[i][each_solution[i]]
#                 solution.append(task_matrix[i][each_solution[i]])
#             values.append(value)
#             solutions.append(solution)
#         min_cost = np.min(values)
#         best_solution = solutions[values.index(min_cost)]
#         return min_cost, best_solution
#
#     # 匈牙利方法
#     def Hungary(self, task_matrix):
#         b = task_matrix.copy()
#         # 行和列减0
#         for i in range(len(b)):
#             row_min = np.min(b[i])
#             for j in range(len(b[i])):
#                 b[i][j] -= row_min
#         for i in range(len(b[0])):
#             col_min = np.min(b[:, i])
#             for j in range(len(b)):
#                 b[j][i] -= col_min
#         line_count = 0
#         # 线数目小于矩阵长度时，进行循环
#         while (line_count < len(b)):
#             line_count = 0
#             row_zero_count = []
#             col_zero_count = []
#             for i in range(len(b)):
#                 row_zero_count.append(np.sum(b[i] == 0))
#             for i in range(len(b[0])):
#                 col_zero_count.append((np.sum(b[:, i] == 0)))
#             # 划线的顺序（分行或列）
#             line_order = []
#             row_or_col = []
#             for i in range(len(b[0]), 0, -1):
#                 while (i in row_zero_count):
#                     line_order.append(row_zero_count.index(i))
#                     row_or_col.append(0)
#                     row_zero_count[row_zero_count.index(i)] = 0
#                 while (i in col_zero_count):
#                     line_order.append(col_zero_count.index(i))
#                     row_or_col.append(1)
#                     col_zero_count[col_zero_count.index(i)] = 0
#             # 画线覆盖0，并得到行减最小值，列加最小值后的矩阵
#             delete_count_of_row = []
#             delete_count_of_rol = []
#             row_and_col = [i for i in range(len(b))]
#             for i in range(len(line_order)):
#                 if row_or_col[i] == 0:
#                     delete_count_of_row.append(line_order[i])
#                 else:
#                     delete_count_of_rol.append(line_order[i])
#                 c = np.delete(b, delete_count_of_row, axis=0)
#                 c = np.delete(c, delete_count_of_rol, axis=1)
#                 line_count = len(delete_count_of_row) + len(delete_count_of_rol)
#                 # 线数目等于矩阵长度时，跳出
#                 if line_count == len(b):
#                     break
#                 # 判断是否画线覆盖所有0，若覆盖，进行加减操作
#                 if 0 not in c:
#                     row_sub = list(set(row_and_col) - set(delete_count_of_row))
#                     min_value = np.min(c)
#                     for i in row_sub:
#                         b[i] = b[i] - min_value
#                     for i in delete_count_of_rol:
#                         b[:, i] = b[:, i] + min_value
#                     break
#         row_ind, col_ind = linear_sum_assignment(b)
#         min_cost = task_matrix[row_ind, col_ind].sum()
#         best_solution = list(task_matrix[row_ind, col_ind])
#         return min_cost, best_solution
#
#
# # 生成开销矩阵
# rd = random.RandomState(10000)
# task_matrix = rd.randint(0, 100, size=(5, 5))
# # 用全排列方法实现任务分配
# ass_by_per = TaskAssignment(task_matrix, 'all_permutation')
# # 用匈牙利方法实现任务分配
# ass_by_Hun = TaskAssignment(task_matrix, 'Hungary')
# print('cost matrix = ', '\n', task_matrix)
# print('全排列方法任务分配：')
# print('min cost = ', ass_by_per.min_cost)
# print('best solution = ', ass_by_per.best_solution)
# print('匈牙利方法任务分配：')
# print('min cost = ', ass_by_Hun.min_cost)
# print('best solution = ', ass_by_Hun.best_solution)
#
#
#
# # C++全排列
# #include<bits/stdc++.h>
# #include<iostream>
# #include<math.h>
# #include<algorithm>
# #include<string.h>
# #include<string>
# #include<stdlib.h>
# #include<stdio.h>
# #include<vector>
# #include<sstream>
# #include<iomanip>
# #include<map>
# #define LL long long         //9223372036854775807(19位) 2的63次方
# #define debug cout<<"******"<<endl;
# #define INF 0x3fffffff
# #define MAX 101000
# using namespace std;
#
# bool cmp(vector<int> a,vector<int> b){
#     for(int i = 0; i < a.size();i++){
#         if(a[i]!=b[i])
#             return a[i]>b[i];
#     }
# }
#
# int main()
# {
#     int T;
#     cin>>T;
#     while(T--)
#     {
#         int num, minCost = MAX, cost=0;
#         int x, y;
#         cin>>num;
#         int c[num+1][num+1],temp[num+1];
#         char ch;
#         while(cin>>x>>y){
#             cin>>c[x][y];
#             if((ch=getchar()) == '\n')
#                 break;
#         }
#         for(int i=1; i<=num; i++){           //输入成本的矩阵值
#             temp[i]=i;                  //设置全排列辅助数组，默认升序
#         }
#         vector<vector<int>> ret;
#         vector<int> tmp;
#         do                              //利用next_permutation函数依次求出数组的全排列
#         {
#             cost=0;
#             tmp.clear();
#             for(int i=1; i<= num; i++)
#                 cost += c[i][temp[i]];
#             if(cost < minCost){
#                 ret.clear();
#                 minCost=cost;           //记录最小代价
#                 for(int j = 1; j <= num; j++)
#                     tmp.push_back(temp[j]);
#             }else if(cost == minCost){
#                 for(int j = 1; j <= num; j++)
#                     tmp.push_back(temp[j]);
#             }
#             if(!tmp.empty())
#                 ret.push_back(tmp);
#         }
#         while(next_permutation(temp+1, temp+1+num));  //下一个全排列
#         sort(ret.begin(),ret.end(),cmp);
#         int len = ret.size();
#         for(int i = 0; i < len - 1; i++){
#             for(int j = 0; j < num - 1; j++)
#                 cout<<ret[i][j]<<" ";
#             cout<<ret[i][num-1]<<",";
#         }
#         for(int j = 0;j < num-1; j++)
#             cout<<ret[len-1][j]<<" ";
#         cout<<ret[len-1][num-1]<<endl;
#     }
#     return 0;
# }
