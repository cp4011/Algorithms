"""公园有n根板凳，已知有ai个人坐在第i根板凳上，现在又来了m个人，他们每个人都会从这n根板凳当中选择一根坐下。假设所有人坐下
之后，所有板凳都坐了若干人（整个过程中没有人会离开板凳），其中人数最多的为k，请你计算出最小可能的k和最大可能的k。
输入
第一行 一个整数n，表示板凳的个数
第二行一个整数m，表示来的人数
接下来n行，每行一个整数ai，表示第i根板凳上坐的人
输出
一行两个整数，用空格隔开，第一个表示最小的可能的k，第二个表示最大的可能的k
输入
2
1
2
1
输出
2 3
"""


import math
n = int(input())
m = int(input())
arr = []
for _ in range(n):
    arr.append(int(input()))

a = max(arr)
k_2 = m + a
s = a*n - sum(arr)
if m <= s:
    k_1 = a
else:
    b = m - s
    k_1 = a + math.ceil(b/n)

print(k_1, k_2)
