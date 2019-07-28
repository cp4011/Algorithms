"""给出方程式 A / B = k, 其中 A 和 B 均为代表字符串的变量， k 是一个浮点型数字。根据已知方程式求解问题，并返回计算结果。
如果结果不存在，则返回 -1.0。
示例 :    给定 a / b = 2.0, b / c = 3.0
问题: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ? 
返回 [6.0, 0.5, -1.0, 1.0, -1.0 ]
输入如下：   equations(方程式) = [ ["a", "b"], ["b", "c"] ],    values(方程式结果) = [2.0, 3.0],
            queries(问题方程式) = [ ["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"] ].
        输入总是有效的。你可以假设除法运算中不会出现除数为0的情况，且不存在任何矛盾的结果。
"""
'''先构造图，使用dict实现，其天然的hash可以在in判断时做到O(1)复杂度。对每个equation如"a/b=v"构造a到b的带权v的有向边和
b到a的带权1/v的有向边，之后对每个query，只需要进行dfs并将路径上的边权重叠乘就是结果了，如果路径不可达则结果为-1。'''


def calcEquation(equations, values, queries):   # 多源最短路径(Floyd本质上是一种动态规划算法)
    # 构造图，equations的第一项除以第二项等于value里的对应值，第二项除以第一项等于其倒数
    graph = {}
    for (x, y), v in zip(equations, values):
        if x in graph:
            graph[x][y] = v
        else:
            graph[x] = {y: v}
        if y in graph:
            graph[y][x] = 1 / v
        else:
            graph[y] = {x: 1 / v}

    # dfs找寻从s到t的路径并返回结果叠乘后的边权重即结果
    def dfs(s, t) -> int:
        if s not in graph:
            return -1
        if t == s:
            return 1
        for node in graph[s].keys():
            if node == t:
                return graph[s][node]
            elif node not in visited:
                visited.add(node)  # 添加到已访问避免重复遍历
                v = dfs(node, t)
                if v != -1:
                    return graph[s][node] * v
        return -1

    # 逐个计算query的值
    res = []
    for qs, qt in queries:
        visited = set()
        res.append(dfs(qs, qt))
    return res
