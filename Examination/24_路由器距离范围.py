"""一条直线上等距离放置了n台路由器。路由器自左向右从1到n编号。第i台路由器到第j台路由器的距离为| i-j |。  每台路由器都有
自己的信号强度，第i台路由器的信号强度为ai。所有与第i台路由器距离不超过ai的路由器可以收到第i台路由器的信号
（注意，每台路由器都能收到自己的信号）。问一共有多少台路由器可以收到至少k台不同路由器的信号。

输入描述:
输入第一行两个数n , k（1≤n , k≤10^5）
第二行n个数, a1 , a2 , a3……… , an（0≤ai≤10^9）
输出描述:
输出一个数，一共有多少台路由器可以收到至少k台不同路由器的信号。

输入例子1:
4 4
3 3 3 3
输出例子1:
4
"""


# 超时 case通过率为20.00%
def func(arr, n, k):
    ans = 0
    count = [1] * n
    for i in range(n):
        for j in range(1, arr[i]+1):
            if i+j < n:
                count[i + j] += 1
            if n-i-1-j >= 0:
                count[n-i-1-j] += 1

    for i in count:
        if i >= k:
            ans += 1
    return ans


n, k = (int(i) for i in input().split())
arr = [int(i) for i in input().split()]
print(func(arr, n, k))
