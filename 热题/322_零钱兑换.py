"""给定不同面额的硬币 coins 和一个总金额 amount。编写一个函数来计算可以凑成总金额所需的最少的硬币个数。如果没有任何一种
硬币组合能组成总金额，返回 -1。
示例 1:
输入: coins = [1, 2, 5], amount = 11
输出: 3
解释: 11 = 5 + 5 + 1
示例 2:
输入: coins = [2], amount = 3
输出: -1
说明:
你可以认为每种硬币的数量是无限的。
"""


class Solution(object):
    def coinChange(self, coins, amount):  # 找出最少的硬币数——组成一个值amount
        """DP:  假设 f(n) 代表要凑齐金额为 n 所要用的最少硬币数量，那么有:f(n) = min(f(n - c1), f(n - c2), ... f(n - cn)) + 1
            其中 c1 ~ cn 为硬币的所有面额。    f(11) = min(f(10), f(9), f(6)) + 1        """
        res = [0 for _ in range(amount + 1)]
        for i in range(1, amount + 1):
            cost = float('inf')
            for c in coins:
                if i - c >= 0:
                    cost = min(cost, res[i - c] + 1)
            res[i] = cost
        if res[amount] == float('inf'):
            return -1
        else:
            return res[amount]

    def coinChange_1(self, coins, amount):  # 找出最少的硬币——组成[1, amount]中所有面值
        dp = [float("inf") for _ in range(amount + 1)]      # 初始化dp数组
        dp[0] = 0               # 当amount=0时，硬币所需数为0
        if 1 not in coins:      # 如果硬币里面没有面值为1的硬币，则无法组成所有的硬币
            return -1
        dp[1] = 1
        for i in range(2, amount + 1):
            min_ = dp[i]
            for j in range(1, i):
                if j in coins and j <= i - j + 1:   # 如果另一部分直接可以用一个硬币代替【j在硬币库中】
                    min_ = min(min_, dp[i - j] + 1)
                else:
                    min_ = min(min_, dp[i - j] + dp[j])
            dp[i] = min_
        return dp[-1]

