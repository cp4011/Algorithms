"""
给定一个二维整型矩阵，已知矩阵的每一行都按照从小到大的顺序排列，每一列也都按照从小到大的顺序排列。现在给出一个数，请写一个函数返回该数是否存在于矩阵中。
矩阵中出现的数字与需要查找的数(k)都为0~100000之间的整数，且矩阵的大小在3000*3000以内。
在保证正确性的基础上，请尽量给出比较高效的解法。请列出你的算法时间复杂度与空间复杂度分别是多少？

输入描述:
输入两个整数m,n, 且 0<m<=3000, 0<n<=3000。
接着输入一个vector<vector<int>> matrix矩阵，大小为m行n列，与一个int k，为需要查找的数字。

输出描述:
输出true或者false，true表示该数k存在于该matrix矩阵中，false表示该数k不存在于该matrix矩阵中。
示例1
输入
3 3
2 3 5
3 4 7
3 5 8
4
输出
true
说明
4位于矩阵的第二行第二列，故输出true
"""


def fun(mat, m, n, k):
    i, j = 0, n - 1
    while i < m and j >= 0:
        if k == mat[i][j]:
            return True
        elif k > mat[i][j]:
            i += 1
        else:
            j -= 1
    return False


line = input().strip().split()
m, n = int(line[0]), int(line[1])
mat = []
for _ in range(m):
     tmp = [int(i) for i in input().split()]
     mat.append(tmp)
k = int(input())
if fun(mat, m, n, k):
    print("true")
else:
    print("false")


# numpy版本
# from numpy import *
# def fun(mat, m, n, k):
#     i, j = 0, n - 1
#     while i < m and j >= 0:
#         if k == mat[i, j]:
#             return True
#         elif k > mat[i, j]:
#             i += 1
#         else:
#             j -= 1
#     return False
# line = input().strip().split()
# m, n = int(line[0]), int(line[1])
# mat = zeros((m, n))
# for a in range(m):
#     mat[a, :] = [int(b) for b in input().split(' ')]
# k = int(input())
# if fun(mat, m, n, k):
#     print("true")
# else:
#     print("false")

