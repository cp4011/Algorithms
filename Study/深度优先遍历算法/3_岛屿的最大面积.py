""" LeetCode 695
给定一个包含了一些 0 和 1的非空二维数组 grid , 一个 岛屿 是由四个方向 (水平或垂直) 的 1 (代表土地) 构成的组合。你可以
假设二维矩阵的四个边缘都被水包围着。找到给定的二维数组中最大的岛屿面积。(如果没有岛屿，则返回面积为0。)
示例 1:
[[0,0,1,0,0,0,0,1,0,0,0,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,1,1,0,1,0,0,0,0,0,0,0,0],
 [0,1,0,0,1,1,0,0,1,0,1,0,0],
 [0,1,0,0,1,1,0,0,1,1,1,0,0],
 [0,0,0,0,0,0,0,0,0,0,1,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,0,0,0,0,0,0,1,1,0,0,0,0]]
对于上面这个给定矩阵应返回 6。注意答案不应该是11，因为岛屿只能包含水平或垂直的四个方向的‘1’。
示例 2:
[[0,0,0,0,0,0,0,0]]
对于上面这个给定的矩阵, 返回 0。
注意: 给定的矩阵grid 的长度和宽度都不超过 50。
"""


class Solution:
    def maxAreaOfIsland(self, grid):
        self.maxArea = 0                                # 存储最大岛屿的面积
        row = len(grid)                                 # 存储地图的行数
        col = len(grid[0])                              # 存储地图的列数
        for i in range(row):
            for j in range(col):                        # 开始从左到右，从上到下的搜索岛屿
                if grid[i][j] == 1:                     # 如果发现了陆地的话
                    current = 1
                    self.dfs(i, j, current, grid)       # 测量岛屿面积，核心代码
        return self.maxArea                             # 最后返回最大岛屿的

    def dfs(self, k, z, current, grid):                 # k,z为点的坐标,current存储目前岛屿的面积，grid为地图
        grid[k][z] = 2                                  # 第一步先标记此处为已访问
        if k > 0 and grid[k - 1][z] == 1:               # 向上走前先考察不越界并且为陆地
            current = self.dfs(k - 1, z, current + 1, grid)         # 递归调用函数，更新x左边和当前面积
        if k < (len(grid) - 1) and grid[k + 1][z] == 1:             # 向下走前先考察不越界并且为陆地
            current = self.dfs(k + 1, z, current + 1, grid)
        if z > 0 and grid[k][z - 1] == 1:                           # 向左走前先考察不越界并且为陆地
            current = self.dfs(k, z - 1, current + 1, grid)
        if z < (len(grid[0]) - 1) and grid[k][z + 1] == 1:          # 向右走前先考察不越界并且为陆地
            current = self.dfs(k, z + 1, current + 1, grid)
        self.maxArea = max(self.maxArea, current)                   # 更新最大面积变量
        return current


# dfs
class Solution:
    def maxAreaOfIsland(self, grid: 'List[List[int]]') -> 'int':
        n, m = len(grid), len(grid[0])

        def dfs(i, j):
            if 0 <= i < n and 0 <= j < m and grid[i][j]:
                grid[i][j] = 0
                return 1 + dfs(i-1, j) + dfs(i+1, j) + dfs(i, j-1) + dfs(i, j+1)
            return 0
        return max((dfs(i, j) for i in range(n) for j in range(m)), default=0)


# dfs
class Solution:
    def maxAreaOfIsland(self, grid: 'List[List[int]]') -> 'int':
        n, m = len(grid), len(grid[0])

        def has_one(i, j):
            return 0 <= i < n and 0 <= j < m and grid[i][j]

        def bfs(i, j):
            if not has_one(i, j): return 0
            que, area, grid[i][j] = collections.deque([(i, j)]), 1, 0
            while que:
                i, j = que.popleft()
                for ni, nj in ((i-1, j), (i+1, j), (i, j-1), (i, j+1)):
                    if has_one(ni, nj):
                        grid[ni][nj] = 0
                        area += 1
                        que.append((ni, nj))
            return area
        return max((bfs(i, j) for i in range(n) for j in range(m)), default=0)
