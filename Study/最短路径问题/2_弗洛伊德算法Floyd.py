"""             时间复杂度:O(n^3) 空间复杂度:O(n^2)
1，从任意一条单边路径开始。所有两点之间的距离是边的权，如果两点之间没有边相连，则权为无穷大。
2，对于每一对顶点 u 和 v，看看是否存在一个顶点 w 使得从 u 到 w 再到 v 比已知的路径更短。如果是更新它。

Floyd算法适用于【多源最短路径】【边权可正可负】，是一种动态规划算法，稠密图效果最佳。此算法简单有效，
由于三重循环结构紧凑，对于稠密图，效率要高于执行|V|次Dijkstra算法，也要高于执行|V|次SPFA算法。
优点：容易理解，可以算出任意两个节点之间的最短距离，代码编写简单。
缺点：【时间复杂度比较高】，不适合计算大量数据
"""
import sys


class Solution:
    def solveFloyd(self, dist, start, end):				            # 参数： 距离矩阵D【无向图时，矩阵关于对角线对称】，起始点， 终点
        n = len(dist)                                               # 距离矩阵D【无向图时，矩阵关于对角线对称，即D[i][j] = D[j][i]】
        path = self.createPath(n)                                   # 创建路径矩阵P
        for k in range(n):						                    # 遍历节点，设【k为中介点】
            for i in range(n):
                for j in range(n):
                    if dist[i][j] > dist[i][k] + dist[k][j]:		# 以k为中介点，如果路程变得更短
                        dist[i][j] = dist[i][k] + dist[k][j]		# 更新D，P矩阵
                        path[i][j] = path[i][k]
        self.printPath(start, path, end)			                # 输出

    def createPath(self, n):				                        # 创建path路径矩阵P。P[i][j]的值：从i节点到j节点的最短路径中经过的第一个节点
        path = []						                            # 一个长度为n，由[0,1,2,3,…,n-1]构成的二维数组
        for i in range(n):
            row = []
            for j in range(n):
                row.append(j)
            path.append(row)                                        # P[i][j] 不一定等于 P[j][i]，两条路径经过的第一个节点有可能不同
        return path                                                 # 返回路线P矩阵

    def printPath(self, current, path, end):			            # 输出方法
        solution = []					                            # solution为最短路线列表
        while current != end:				                        # 只要当前节点不为终点
            solution.append(current)		                        # 把当前节点加入solution
            current = path[current][end]	                        # 设当前节点为路线中的下一个节点
        solution.append(current)			                        # 最后加入终点
        print(solution)					                            # 输出solution


Solution().solveFloyd([[0, 10, 15, sys.maxsize, 30, sys.maxsize],
                       [10, 0, sys.maxsize, 5, 14, sys.maxsize],
                       [15, sys.maxsize, 0, 12, 12, sys.maxsize],
                       [sys.maxsize, 5, 12, 0, sys.maxsize, 10],
                       [30, 14, 12, sys.maxsize, 0, 20],
                       [sys.maxsize, sys.maxsize, sys.maxsize, 10, 20, 0]], 0, 5)       # 输出0节点到5节点的路劲
