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


class Solution:                             # 网格中有障碍物。那么从左上角到右下角将会有多少条不同的路径
    def uniquePathsWithObstacles(self, obstacleGrid):
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[1] * n for _ in range(m)]

        for i in range(n):                  # 初始第一行中的各列边界
            if obstacleGrid[0][i] == 1:
                for j in range(i, n):       # 语法错误 dp[0][i:] = 0：切片复制给 整型0 不具有迭代能力，
                    dp[0][j] = 0            # dp[0][i:] = (0,)将切片的所有元素换成0，此处若使用，则后续遍历的时列表短了,数组下标越界
                break                       # 注意break不要放到for循环中了
        for i in range(m):
            if obstacleGrid[i][0] == 1:     # 初始第一列中的各行边界
                for j in range(i, m):
                    dp[j][0] = 0
                break

        for i in range(1, m):               # 注意从1开始遍历【边界已经初始化了】
            for j in range(1, n):
                if obstacleGrid[i][j] == 0:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
                else:
                    dp[i][j] = 0            # obstacleGrid[i][j]=1 的全部置为0，表示没有路径可以达到
        return dp[-1][-1]


