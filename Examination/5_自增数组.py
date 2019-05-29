"""自增数组
小Q发现了一种特殊的数组，叫做自增数组。
这个数组支持一种操作：每次操作可以把数组中一个数自增1。
现在有一个长度为n的自增数组，小Q现在想利用这个操作把数组中的每个数都变得不一样，请问你最少需要多少次操作？
输入描述
第一行，一个整数n (n <= 10000)
第二行，n个空格间隔的整数，即数组中的元素ai(-10000 <= ai <= 10000)。
输出描述
一个整数，表示最少需要操作的次数
示例1
输入
5
1 2 3 2 5
输出
2
"""

def func(arr):
    n = len(arr)
    re = dict()
    for i in range(n-1):
        if arr[i] == arr[i+1]:
            re[i+1] = arr[i+1]
    return re

n = int(input())
arr = list(map(int, input().split()))
arr.sort()
arr1 = arr[:]
r = func(arr)

for key, value in r.items():
    val = value + 1
    while val in arr:
        val += 1
    arr[key] = val
ans = 0
for i in range(n):
    ans = ans + (arr[i]-arr1[i])
print(ans)


# 30%
# def fun(n, arr):
#     ans = 0
#     for i in range(n):
#         while arr.count(arr[i]) != 1:
#             arr[i] += 1
#             ans += 1
#     return ans
#
# n = int(input())
# arr = [int(i) for i in input().split()]
# print(fun(n, arr))
