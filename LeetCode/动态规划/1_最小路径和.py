"""给定一个包含非负整数的 m x n 网格，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。
说明：每次只能向下或者向右移动一步。
示例:
输入:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
输出: 7
解释: 因为路径 1→3→1→1→1 的总和最小。
"""


class Solution:
    def minPathSum(self, grid):
        if not grid or grid[0] == []:
            return 0
        rows, cols = len(grid), len(grid[0])
        dp = [[0] * cols for _ in range(rows)]
        dp[0][0] = grid[0][0]                           # 初始化左上角第一个元素

        for i in range(1, cols):                        # 初始化第一行row        【注意从 1 开始初始化】
            dp[0][i] = dp[0][i - 1] + grid[0][i]

        for i in range(1, rows):                        # 初始化第一列cols       【注意从 1 开始初始化】
            dp[i][0] = dp[i - 1][0] + grid[i][0]

        for i in range(1, rows):                        # 取row, column 跟当前元素相加的最小值
            for j in range(1, cols):
                dp[i][j] = min(dp[i - 1][j] + grid[i][j], dp[i][j - 1] + grid[i][j])

        return dp[-1][-1]

    #  O(mn) time O(1) space In place
    def minPathSum1(self, grid):
        if not grid or grid[0] == []:
            return 0
        R, C = len(grid), len(grid[0])
        for i in range(R):
            for j in range(C):
                if i != 0 or j != 0:
                    grid[i][j] += min(grid[i - 1][j] if i > 0 else float("Inf"),
                                      grid[i][j - 1] if j > 0 else float("Inf"))
        return grid[-1][-1]
