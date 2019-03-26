"""零钱兑换(硬币最小数量)  LeetCode 322
给定不同面额的硬币 coins 和一个总金额 amount。编写一个函数来计算可以凑成总金额所需的最少的硬币个数。如果没有任何一种硬币
组合能组成总金额，返回 -1。   你可以认为每种硬币的数量是无限的。
示例 1:
输入: coins = [1, 2, 5], amount = 11
输出: 3
解释: 11 = 5 + 5 + 1
示例 2:
输入: coins = [2], amount = 3
输出: -1
"""


# 动态规划
def coinChange(coins, amount):
    if amount == 0 or len(coins) == 0:
        return 0
    dp = [0 if i == 0 else float("inf") for i in range(amount + 1)]
    for i in range(1, amount + 1):
        for coin in coins:
            if i >= coin:
                dp[i] = min(dp[i], dp[i - coin] + 1)
    return dp[-1] if dp[-1] <= amount else -1

# print(coinChange([186, 83, 408, 419], 6249))
# print(coinChange([1, 2, 5], 11))


# 自己（错误）
def fun(arr, n, amount):
    arr.sort()
    a = amount // arr[-1]
    b = amount % arr[-1]
    for coin in arr[n-2::-1]:
        a += b // coin
        b = b % coin
    if b != 0:
        return -1
    return a

# print(fun([83, 186, 408, 419], 4, 6249))            # 应该输出20，但是输出的是-1
