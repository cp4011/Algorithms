"""一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）。
机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。
问总共有多少条不同的路径？
说明：m 和 n 的值均不超过 100。
示例 1:

输入: m = 3, n = 2
输出: 3
解释:
从左上角开始，总共有 3 条路径可以到达右下角。
1. 向右 -> 向右 -> 向下
2. 向右 -> 向下 -> 向右
3. 向下 -> 向右 -> 向右

示例 2:
输入: m = 7, n = 3
输出: 28
"""

'''【组合问题】 机器人一定会走m+n-2步，即从m+n-2中挑出m-1步向下走不就行了吗？即C（（m+n-2），（m-1））。'''

'''【动态规划】向下+向左 dp[m, n] = dp[m-1, n] + dp[m, n-1]  边界dp[m, 1], dp[1, m] = 1, 1  构造初始查询列表，当n=1时 初始值路径都为1'''

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[1] * n for _ in range(m)]        # 二维数组，初始化为1
        for i in range(1, m):                   # 【注意从1开始的】
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[-1][-1]

    def uniquePaths2(self, m: int, n: int) -> int:
        dp = [1] * n                            # 一维数组即可，并初始化为1（边界值都为1）
        for i in range(1, m):                   # 【注意从1开始的】
            for j in range(1, n):
                dp[j] = dp[j-1] + dp[j]
        return dp[-1]
