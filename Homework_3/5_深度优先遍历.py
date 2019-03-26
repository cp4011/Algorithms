'''深度优先遍历
Description
按照给定的起始顶点深度优先遍历给定的无向图，尝试所有可能的遍历方式，打印遍历过程中出现的最大深度。
Input
输入第一行是用例个数，后面每个用例使用多行表示，用例的第一行是图中节点的个数n和起始点，用空格隔开，后面n+1行为图的邻接矩阵，其中第一行为节点名称。值之间使用空格隔开。
Output
输出深度优先遍历中遇到的最大深度。
Sample Input 1
1
4 a
a b c d
a 0 1 1 0
b 1 0 1 0
c 1 1 0 1
d 0 0 1 0
Sample Output 1
4
'''


# 方法1
class Graph(object):
    def __init__(self):
        self.node_neighbors = {}
        self.visited = {}

    def add_nodes(self, nodelist):
        for node in nodelist:
            self.add_node(node)

    def add_node(self, node):
        if node not in self.nodes():
            self.node_neighbors[node] = []

    def nodes(self):
        return self.node_neighbors.keys()

    def add_edge(self, edge):
        u, v = edge
        if (v not in self.node_neighbors[u]) and (u not in self.node_neighbors[v]):
            self.node_neighbors[u].append(v)

            if u != v:
                self.node_neighbors[v].append(u)

    def depth_first_search(self, root=None):
        def dfs(node, length, max_len_list):    # 定义dfs函数体
            self.visited[node] = True
            # print("node: %s, visited: %s" % (node, self.visited))

            flag = True
            for n in self.node_neighbors[node]:
                if n not in self.visited or not self.visited[n]:
                    flag = False
                    dfs(n, length+1, max_len_list)
                    self.visited[n] = False

            if flag:
                max_len_list.append(length)

        if root:                  # 执行dfs函数
            tmp_max_len = []
            dfs(root, 1, tmp_max_len)
            print(max(tmp_max_len))     # tmp_max_len为 [4,3,3]


num_case = int(input())
for _ in range(num_case):
    N, start = input().split(" ")
    N = int(N)
    labels = input().split(" ")
    g = Graph()
    g.add_nodes(labels)
    for i in range(N):
        line = input().split(" ")
        cur_label = line[0]
        edges = list(map(int, line[1:]))
        for index, value in enumerate(edges):
            if value != 0:
                g.add_edge((cur_label, labels[index]))

    g.depth_first_search(start)


# 方法2
# def findMaxLen(start, array):
#     global max
#     global step
#     global visited
#     visited[start] = 1
#     for i in range(len(array[start])):
#         if array[start][i] == '1' and visited[i] == 0:
#             step += 1
#             if step > max:
#                 max = step
#             findMaxLen(i, array)
#             visited[i] = 0
#             step -= 1
#
#
# num = int(input())
# for i in range(num):
#     args = input().split(' ')
#     n = int(args[0])
#     startName = args[1]
#     nodeNames = input().split(' ')
#
#     arrays = []
#     num_arrays = []
#     for j in range(n):
#         line = input().split(' ')
#         arrays.append(line)
#
#     for j in range(n):
#         num_arrays.append(arrays[j][1:])
#
#     start = 0
#
#     for k in range(n):
#         if nodeNames[k] == args[1]:
#             start = k
#             break
#     global max
#     global step
#     global visited
#     max = 1
#     step = 1
#     visited = [0 for i in range(n)]
#     findMaxLen(start, num_arrays)
#     print(max)




# 图的深度优先遍历 (栈）
# 1.利用栈实现
# 2.从源节点开始把节点按照深度放入栈，然后弹出
# 3.每弹出一个点，把该节点下一个没有进过栈的邻接点放入栈
# 4.直到栈变空
# def dfs(node):
#     if node is None:
#         return
#     nodeSet = set()
#     stack = []
#     print(node.value)
#     nodeSet.add(node)
#     stack.append(node)
#     while len(stack) > 0:
#         cur = stack.pop()               # 弹出最近入栈的节点
#         for next in cur.nexts:         # 遍历该节点的邻接节点
#             if next not in nodeSet:    # 如果邻接节点不重复
#                 stack.append(cur)       # 把节点压入
#                 stack.append(next)      # 把邻接节点压入
#                 set.add(next)           # 登记节点
#                 print(next.value)       # 打印节点值
#                 break                   # 退出，保持深度优先

# 深度优先遍历(由于python没有直接的实现栈，这里使用了list来模拟，入栈就是向列表中append一个元素，出栈就是取列表最后一个元素然后pop将最后一个元素删除)
# def dfs(adj, start):
#     visited = set()
#     stack = [[start, 0]]
#     while stack:
#         (v, next_child_idx) = stack[-1]
#         if (v not in adj) or (next_child_idx >= len(adj[v])):
#             stack.pop()
#             continue
#         next_child = adj[v][next_child_idx]
#         stack[-1][1] += 1
#         if next_child in visited:
#             continue
#         print(next_child)
#         visited.add(next_child)
#         stack.append([next_child, 0])
# graph = {1: [4, 2], 2: [3, 4], 3: [4], 4: [5]}
# dfs(graph, 1)
