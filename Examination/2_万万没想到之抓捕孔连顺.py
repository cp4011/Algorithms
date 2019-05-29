""" 1. 我们在字节跳动大街的N个建筑中选定3个埋伏地点。
    2. 为了相互照应，我们决定相距最远的两名特工间的距离不超过D。
请听题：给定N（可选作为埋伏点的建筑物数）、D（相距最远的两名特工间的距离的最大值）以及可选建筑的坐标，计算在这次行动中，
大锤的小队有多少种埋伏选择。
注意：
1. 两个特工不能埋伏在同一地点
2. 三个特工是等价的：即同样的位置组合(A, B, C) 只算一种埋伏方法，不能因“特工之间互换位置”而重复使用
输入描述:
第一行包含空格分隔的两个数字 N和D(1 ≤ N ≤ 1000000; 1 ≤ D ≤ 1000000)
第二行包含N个建筑物的的位置，每个位置用一个整数（取值区间为[0, 1000000]）表示，从小到大排列（将字节跳动大街看做一条数轴）
输出描述:
一个数字，表示不同埋伏方案的数量。结果可能溢出，请对 99997867 取模

输入例子1:
4 3
1 2 3 4
输出例子1:
4
例子说明1:
可选方案 (1, 2, 3), (1, 2, 4), (1, 3, 4), (2, 3, 4)

输入例子2:
5 19
1 10 20 30 50
输出例子2:
1
例子说明2:
可选方案 (1, 10, 20)
"""


MOD = 99997867
def solve(n, d, nums):
    """考虑d足够大的情况:1,2,3 -> C(3,3) = 1    1,2,3,4 -> C(4,3) = 4 = 1 + C(3,2)  1,2,3,4,5 -> C(5,3) = 10 = 4 + C(4,2)
    相当于 固定了最后一个确定的元素5，再前面n个元素中任意选两个C(n,2)           定义dp[i]: 以nums[i]为最大元素的方案数
    由于nums是递增的,j不用每次都从0重新开始向右滑动, i: 遍历到的数字    j: 与i相差距离>d的最近的坐标索引  """
    dp = [0] * n
    dp[2] = 1 if nums[2] - nums[0] <= d else 0
    j = 0                                           # 定义j从左到右滑动
    for i in range(3, n):
        while j < i and nums[i] - nums[i] > d:      # j刚好与i的距离 <= d，循环结束
            j += 1
        c = i - j               # i前面一共有 i-j 个元素，如例1(距离为1 2 3 4)：索引j=0，i=3时结束循环，4(i=3)前面有三个元素，3选2
        dp[i] = c * (c - 1) // 2 if c >= 3 else 0
        dp[i] %= MOD
    return sum(dp) % MOD


N, D = list(map(int, input().split()))
nums = list(map(int, input().split()))
print(solve(N, D, nums))


def solve2(n, d, nums):
    """  dp[i] 以nums[i]为最大元素的方案数  30%超时    """
    dp = [0] * n
    dp[2] = 1 if nums[2] - nums[0] <= d else 0
    for i in range(3, n):
        c = 0
        j = i - 1                                   # 定义j从右到左滑动，可能d太大，需要滑动太久，超时
        while j >= 0 and nums[i] - nums[j] <= d:
            c += 1
            j -= 1
        dp[i] = c * (c - 1) // 2 if c >= 3 else 0
        dp[i] %= MOD
    return sum(dp) % MOD


# 超时 case通过率为20.00%
def func(arr, d):
    from itertools import combinations
    c = combinations(arr, 3)
    ans = []
    for i in c:
        if i[2] - i[0] <= d:
            ans.append(i)
    return len(ans) % 99997867


n, d = (int(i) for i in input().split())
arr = [int(i) for i in input().split()]
print(func(arr, d))
