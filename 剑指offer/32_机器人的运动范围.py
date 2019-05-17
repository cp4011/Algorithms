"""地上有一个m行和n列的方格。一个机器人从坐标0,0的格子开始移动，每一次只能向左，右，上，下四个方向移动一格，但是不能进入
行坐标和列坐标的数位之和大于k的格子。 例如，当k为18时，机器人能够进入方格（35,37），因为3+5+3+7 = 18。但是，它不能进入
方格（35,38），因为3+5+3+8 = 19。请问该机器人能够达到多少个格子？
"""

'''回溯法
    1.从(0,0)开始走，每成功走一步标记当前位置为true,然后从当前位置往四个方向探索，返回1 + 4 个方向的探索值之和。
    2.探索时，判断当前节点是否可达的标准为：
        1）当前节点在矩阵内；
        2）当前节点未被访问过；
        3）当前节点满足limit限制。
'''
# 【x, y 各数位之和】      sum(map(int, str(x) + str(y)))


class Solution:
    def movingCount(self, threshold, rows, cols):
        vis = [[0 for _ in range(cols)] for _ in range(rows)]       # 注意显示cols，再是rows

        def DFS(x, y):      # 从 (x, y) 开始走
            if 0 <= x < rows and 0 <= y < cols and vis[x][y] == 0 and sum(map(int, str(x) + str(y))) <= threshold:
                vis[x][y] = 1
                # 四个方向进行求和，每执行一次接下来的 return 说明有一个点满足条件，对应加 1
                return 1 + DFS(x - 1, y) + DFS(x + 1, y) + DFS(x, y - 1) + DFS(x, y + 1)
            return 0

        return DFS(0, 0)        # 从 (0, 0) 开始走
