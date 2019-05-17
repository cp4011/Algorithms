"""一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）。
机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。
现在考虑网格中有障碍物。那么从左上角到右下角将会有多少条不同的路径？
网格中的障碍物和空位置分别用 1 和 0 来表示。

说明：m 和 n 的值均不超过 100。
示例 1:
输入:
[
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
输出: 2
解释:
3x3 网格的正中间有一个障碍物。
从左上角到右下角一共有 2 条不同的路径：
1. 向右 -> 向右 -> 向下 -> 向下
2. 向下 -> 向下 -> 向右 -> 向右
"""


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[1] * n for _ in range(m)]

        for i in range(n):                      # 初始化边界 第一行
            if obstacleGrid[0][i] == 1:
                for j in range(i, n):           # 只要边界上有阻碍，这第一行后面的都为0，因为只能向下或者向右走
                    dp[0][j] = 0
                break
        for i in range(m):                      # 初始化边界 第一列
            if obstacleGrid[i][0] == 1:
                for j in range(i, m):
                    dp[j][0] = 0
                break

        for i in range(1, m):                   # 【注意从1开始】，边界以及初始化了，并且下面有i-1
            for j in range(1, n):
                if obstacleGrid[i][j] == 0:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
                else:
                    dp[i][j] = 0
        return dp[-1][-1]



