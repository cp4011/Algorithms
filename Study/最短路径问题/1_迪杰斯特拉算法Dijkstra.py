"""迪杰斯特拉算法解决【图的单源最短路径问题】【要求权重不为负数】，一个点（源点）到其余各个顶点的最短路径。Dijkstra算法时间复杂度O(n2)"""

"""Dijkstra算法的主要思想：通过“边”来松弛该源点到其余各个顶点的距离。"""
"""算法的基本思想是：每次找到离源点（1号顶点）最近的一个顶点，然后以该顶点为中心进行扩展，最终得到源点到其余所有点的
最短路径。基本步骤如下：
    1.将所有的顶点分为两部分：已知最短路程的顶点集合P和未知最短路径的顶点集合Q。最开始，已知最短路径的顶点集合P中只有
源点一个顶点。我们这里用一个book[i]数组来记录哪些点在集合P中。例如对于某个顶点i，如果book[i]为1则表示这个顶点在集合P中，
如果book[i]为0则表示这个顶点在集合Q中。
    2.设置源点s到自己的最短路径为0即dis=0。若存在源点有能直接到达的顶点i，则把dis[i]设为e[s][i]。同时把所有其它
（源点不能直接到达的）顶点的最短路径为设为∞。
    3.在集合Q的所有顶点中选择一个离源点s最近的顶点u（即dis[u]最小）加入到集合P。并考察所有以点u为起点的边，对每一条边进行
松弛操作。例如存在一条从u到v的边，那么可以通过将边u->v添加到尾部来拓展一条从s到v的路径，这条路径的长度是dis[u]+e[u][v]。
如果这个值比目前已知的dis[v]的值要小，我们可以用新值来替代当前dis[v]中的值。
    4.重复第3步，如果集合Q为空，算法结束。最终dis数组中的值就是源点到所有顶点的最短路径。
"""
from collections import defaultdict
import sys


class Graph:                                    # Graph类：图【节点、边、距离】的定义
    def __init__(self):
        self.nodes = set()                      # 结点集合
        self.edges = defaultdict(list)          # 边集合的字典
        self.distances = {}                     # 边的距离的集合

    def add_node(self, value):                  # 添加结点
        self.nodes.add(value)

    def add_edge(self, from_node, to_node, distance):  # 添加边
        self.edges[from_node].append(to_node)
        self.distances[(from_node, to_node)] = distance


class Node:                                     # 结点类：节点【节点名、前任节点、距离】的定义
    def __init__(self, name):
        self.distance = sys.maxint              # 距离值
        self.predecessor = None                 # 前任结点
        self.name = name                        # 名称

    def set_distance(self, dist):               # 设距离值
        self.distance = dist

    def set_predecessor(self, pred):            # 设前任结点
        self.predecessor = pred

    def get_distance(self):                     # 得到距离值
        return self.distance

    def get_predecessor(self):                  # 得到前任结点
        return self.predecessor


def dijsktra(graph, initial, end):
    permanent = {}                              # 永久集合
    temporary = {}                              # 临时集合
    temporary.add(initial)                      # 起点加入临时集合
    initial.set_distance(0)                     # 设起点距离值为0

    while temporary:                            # 只要临时集合不为空
        min_node = None
        for node in temporary:                  # 找临时集合中距离值最少的结点
            if min_node is None:
                min_node = node
            elif node.get_distance() < min_node.get_distance():
                min_node = node
        temporary.remove(min_node)                              # 把找到的距离最小的该结点从临时集合移除
        permanent.add(min_node)                                 # 加结点到永久集合
        current_distance = min_node.get_distance()
        for neighbour in graph.edges[min_node]:                 # 遍历当前节点的每一个相邻结点
            new_distance = current_distance + graph.distance[(min_node, neighbour)]
            if neighbour not in permanent and new_distance < neighbour.get_distance():  # 若新的距离小于相邻节点的距离值
                neighbour.set_distance(new_distance)            # 更新相邻节点的距离值
                neighbour.set_predecessor(min_node)             # 更新相邻节点的前任
                temporary.add(neighbour)                        # 成功更新距离后，将相邻节点加入临时节点结合中


def printPath(self, end, predecessor):              # 输出路线方法
    current = end
    path = {end}                                    # 路线结点集合
    while current.predecessor != None:              # 只要当前结点有前任结点
        path.add(current.predecessor)               # 把前任结点加入集合
        current = current.predecessor               # 更新当前结点
    path.reverse()                                  # 翻转集合
    print(path)                                     # 输出集合

