"""小易有一些立方体，每个立方体的边长为1，他用这些立方体搭了一些塔。
现在小易定义：这些塔的不稳定值为它们之中最高的塔与最低的塔的高度差。
小易想让这些塔尽量稳定，所以他进行了如下操作：每次从某座塔上取下一块立方体，并把它放到另一座塔上。
注意，小易不会把立方体放到它原本的那座塔上，因为他认为这样毫无意义。
现在小易想要知道，他进行了不超过k次操作之后，不稳定值最小是多少。

输入描述:
第一行两个数n,k (1 <= n <= 100, 0 <= k <= 1000)表示塔的数量以及最多操作的次数。
第二行n个数，ai(1 <= ai <= 104)表示第i座塔的初始高度。

输出描述:
第一行两个数s, m，表示最小的不稳定值和操作次数(m <= k)
接下来m行，每行两个数x,y表示从第x座塔上取下一块立方体放到第y座塔上。
示例1
输入
3 2
5 8 5
输出
0 2
2 1
2 3
"""
'''思路： 其实很简单，每次排个序，然后从最大堆往最小堆搬一个即可，并记录堆序号，直到最大堆-最小堆<1 或者 移动次数达到k。
这里排序并保留堆序号的方法，是用的python内置的sort()函数，当然也可以调用 numpy的argsort()。
'''

n, k = list(map(int, input().split()))
arr = list(map(int, input().split()))

# index_arr = [[1, 5], [2, 8], [3, 5]] 其中每个元素表示：[第i堆，对应塔数]
index_arr = [list(i) for i in zip(range(1, len(arr)+1), arr)]               # 【zip()函数】或者用列表枚举
# index_arr = [[index, arr] for index, arr in enumerate(arr, 1)]            # enumerate(sequence, [start=0])
# 将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，同时列出数据和数据下标，一般用在 for 循环当中

sorted_arr = sorted(index_arr, key=lambda x: x[1], reverse=True)
res = []
count = 0

while k > count and sorted_arr[0][1] > sorted_arr[-1][1]:
    sorted_arr[0][1] -= 1
    sorted_arr[-1][1] += 1
    res.append([sorted_arr[0][0], sorted_arr[-1][0]])
    count += 1
    sorted_arr = sorted(sorted_arr, key=lambda x: x[1], reverse=True)

s = sorted_arr[0][1] - sorted_arr[-1][1]
print(s, k)
for i in res:
    print(i[0], i[1])

