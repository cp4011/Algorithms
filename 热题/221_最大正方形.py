"""在一个由 0 和 1 组成的二维矩阵内，找到只包含 1 的最大正方形，并返回其面积。
示例: 输入:
1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0
输出: 4
"""


class Solution:
    def maximalSquare(self, matrix):
        length = 0
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return 0
        dp = [[0] * len(matrix[0]) for _ in range(len(matrix))]  # dp[i][j]表示以(i,j)处作为正方形右下角,由1组成的最大正方形的边长
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == "1":                 # 元素为"1"时
                    if i == 0 or j == 0:                # 如果在边界处，dp[i][j] = 1表示以该处作为右下角的最大边长为1
                        dp[i][j] = 1
                    else:
                        dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + 1    # 取三者中的较小值 + 1
                    length = max(length, dp[i][j])      # 记录过程中的最大边长
        return length * length
