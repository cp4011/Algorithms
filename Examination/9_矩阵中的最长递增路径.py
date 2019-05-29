"""给定一个整数矩阵，找出最长递增路径的长度。
对于每个单元格，你可以往上，下，左，右四个方向移动。 你不能在对角线方向上移动或移动到边界外（即不允许环绕）。
示例 1:
输入: nums =
[
  [9,9,4],
  [6,6,8],
  [2,1,1]
]
输出: 4
解释: 最长递增路径为 [1, 2, 6, 9]。
示例 2:

输入: nums =
[
  [3,4,5],
  [3,2,6],
  [2,2,1]
]
输出: 4
解释: 最长递增路径是 [3, 4, 5, 6]。注意不允许在对角线方向上移动。
"""


# DP + DFS
class Solution:
    def longestIncreasingPath(self, matrix) -> int:
        if not matrix or not matrix[0]:
            return 0
        m, n = len(matrix), len(matrix[0])
        dp = {}
        max_length = 1
        def dfs(i, j, dp):
            if (i, j) in dp:
                return dp[(i, j)]
            a = 1
            if i > 0 and matrix[i][j] < matrix[i - 1][j]:
                a = max(a, 1 + dfs(i - 1, j, dp))           # 注意要 【1 + dfs()】
            if i + 1 < m and matrix[i][j] < matrix[i + 1][j]:
                a = max(a, 1 + dfs(i + 1, j, dp))
            if j > 0 and matrix[i][j] < matrix[i][j - 1]:
                a = max(a, 1 + dfs(i, j - 1, dp))
            if j + 1 < n and matrix[i][j] < matrix[i][j + 1]:
                a = max(a, 1 + dfs(i, j + 1, dp))
            dp[(i, j)] = a
            return dp[(i, j)]
        for i in range(m):
            for j in range(n):
                max_length = max(max_length, dfs(i, j, dp))
        return max_length


def longestIncreasingPath(matrix):
    def dfs(i, j):
        if not dp[i][j]:
            val = matrix[i][j]
            dp[i][j] = 1 + max(
                dfs(i - 1, j) if i and val > matrix[i - 1][j] else 0,
                dfs(i + 1, j) if i < m - 1 and val > matrix[i + 1][j] else 0,
                dfs(i, j - 1) if j and val > matrix[i][j - 1] else 0,
                dfs(i, j + 1) if j < n - 1 and val > matrix[i][j + 1] else 0)
        return dp[i][j]

    if not matrix or not matrix[0]:
        return 0
    m, n = len(matrix), len(matrix[0])
    dp = [[0] * n for _ in range(m)]
    return max((dfs(x, y) for x in range(m) for y in range(n)), default=0)






