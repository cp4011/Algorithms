'''广度优先遍历图
Description
按照给定的起始顶点广度优先遍历图，每一次通过字母顺序选择顶点查找下一层邻接点，打印遍历顺序。
Input
输入第一行为测试用例个数，后面每一个用例用多行表示，用例第一行是节点个数n和开始顶点，用空格隔开，后面n+1行为图的邻接矩阵，其中第一行为节点名称。值之间使用空格隔开。
Output
输出遍历顺序，用空格隔开
Sample Input 1
1
4 a
a b c d
a 0 1 1 0
b 1 0 1 0
c 1 1 0 1
d 0 0 1 0
Sample Output 1
a b c d
'''


# 方法1
class Graph(object):
    def __init__(self):
        self.node_neighbors = {}
        self.visited = {}       #注意应该使用 字典

    def add_nodes(self, nodelist):
        for node in nodelist:
            self.add_node(node)

    def add_node(self, node):
        if node not in self.node_neighbors:
            self.node_neighbors[node] = []

    def nodes(self):
        return self.node_neighbors.keys()

    def add_edge(self, edge):
        u, v = edge
        if (u not in self.node_neighbors[v]) or (v not in self.node_neighbors[u]):
            self.node_neighbors[u].append(v)

            if u != v:
                self.node_neighbors[v].append(u)

    def breadth_first_search(self, root=None):
        queue = [root]      # 待遍历的节点 把起始节点a放入队列
        order = [root]      # 遍历的顺序    第一个遍历a
        self.visited[root] = True       # 申明节点a已经被遍历了

        while len(queue) > 0:           # 当队列中还有未遍历的节点
            cur_node = queue.pop(0)     # 取出队列中的头结点 a（已经被遍历了，用来找出其相邻的 尚未遍历的节点） 如用已经遍历了的节点c来找到其相邻的节点d，这样才能遍历完所有的节点
            for node in self.node_neighbors[cur_node]:  # 依次遍历当前节点的相邻节点（广度优先遍历） node分别取b，c
                if node not in self.visited:        # 判断是否已经被遍历过了，如果已经被遍历过了，其相邻节点也被找到了 b第一轮尚未被遍历过
                    order.append(node)              # 遍历节点b
                    queue.append(node)              # 并将节点b压入队列中，以找到节点b的相邻节点
                    self.visited[node] = True

        print(" ".join(order))


num_case = int(input())
for _ in range(num_case):
    N, start = input().split(" ")
    N = int(N)
    labels = input().split(" ")
    g = Graph()
    g.add_nodes(labels)
    for i in range(N):
        line = input().split(" ")
        cur_node = line[0]
        edges = list(map(int, line[1:]))
        for index, value in enumerate(edges):
            if value != 0:
                g.add_edge((cur_node, labels[index]))

    g.breadth_first_search(start)

# 方法2
# from queue import Queue
# def BFS(graph, visted, named, start):
#     resultstr = ''
#     n = len(graph)
#     q = Queue();
#     q.put(start)
#     visted[start] = 1
#     resultstr += named[start] + ' '
#
#     while not q.empty():
#         cur = q.get();
#         for i in range(n):
#             if (visted[i] == 0) & (graph[cur][i] == 1):
#                 q.put(i)
#                 visted[i] = 1
#                 resultstr += named[i] + ' '
#     resultstr = resultstr[:-1]
#     print(resultstr)
#
#
# t = int(input())
# for i in range(t):
#     n, startChar = input().split(' ')
#     visted = [0] * int(n)
#     named = input().split(' ')
#     start = named.index(startChar)
#     graph = []
#     for j in range(int(n)):
#         line = input().split(' ')[1:]
#         line = [int(item) for item in line]
#         graph.append(line)
#
#     BFS(graph, visted, named, start)


# 广度优先 遍历树结构
def level_queue(root):
    if root is None:
        return
    my_queue = []
    node = root
    my_queue.append(node)
    while my_queue:
        node = my_queue.pop(0)
        print(node.elem)
        if node.lchild is not None:
            my_queue.append(node.lchild)
        if node.rchild is not None:
            my_queue.append(node.rchild)


# 深度/广度优先遍历(第5 7题综合）
# class Graph(object):
#
#     def __init__(self):
#         self.node_neighbors = {}
#         self.visited = {}
#
#     def add_nodes(self, nodelist):
#         for node in nodelist:
#             self.add_node(node)
#
#     def add_node(self,node):
#         if node not in self.nodes():
#             self.node_neighbors[node] = []
#
#     def add_edge(self, edge):
#         u, v = edge
#         if(v not in self.node_neighbors[u]) and (u not in self.node_neighbors[v]):
#             self.node_neighbors[u].append(v)
#
#             if u != v:
#                 self.node_neighbors[v].append(u)
#
#     def nodes(self):
#         return self.node_neighbors.keys()
#
#     def depth_first_search(self, root=None):
#
#         def dfs(node, length, max_len_list):
#             self.visited[node] = True
#
#             # print("node: %s, visited: %s" % (node, self.visited))
#
#             flag = True
#             for n in self.node_neighbors[node]:
#                 if n not in self.visited or not self.visited[n]:
#                     flag = False
#                     dfs(n, length+1, max_len_list)
#                     self.visited[n] = False
#
#             if flag:
#                 max_len_list.append(length)
#
#         if root:
#             tmp_max_len = []
#             dfs(root, 1, tmp_max_len)
#             print(max(tmp_max_len))
#
#     def breadth_first_search(self, root=None):
#         queue = [root]
#         order = [root]
#         self.visited[root] = True
#
#         while len(queue) > 0:
#             cur_node = queue.pop(0)
#             for node in self.node_neighbors[cur_node]:
#                 if node not in self.visited:
#                     self.visited[node] = True
#                     queue.append(node)
#                     order.append(node)
#
#         print(" ".join(order))
#
#
# num_case = int(input())
# for _ in range(num_case):
#     g = Graph()
#     N, start = input().split(" ")
#     N = int(N)
#     labels = input().split(" ")
#     g.add_nodes(labels)
#     for i in range(N):
#         line = input().split(" ")
#         cur_label = line[0]
#         edges = list(map(int, line[1:]))
#         for index, value in enumerate(edges):
#             if value != 0:
#                 g.add_edge((cur_label, labels[index]))
#
#     # g.depth_first_search(start)
#     g.breadth_first_search(start)



# 图的广度优先遍历
# 1.利用队列实现
# 2.从源节点开始依次按照宽度进队列，然后弹出
# 3.每弹出一个节点，就把该节点所有没有进过队列的邻接点放入队列
# 4.直到队列变空
# from queue import Queue
# def bfs(node):
#     if node is None:
#         return
#     queue = Queue()
#     nodeSet = set()
#     queue.put(node)
#     nodeSet.add(node)
#     while not queue.empty():
#         cur = queue.get()               # 弹出元素
#         print(cur.value)                # 打印元素值
#         for next in cur.nexts:          # 遍历元素的邻接节点
#             if next not in nodeSet:     # 若邻接节点没有入过队，加入队列并登记
#                 nodeSet.add(next)
#                 queue.put(next)

#广度优先遍历
# from queue import Queue
# def bfs(adj, start):
#     visited = set()
#     q = Queue()
#     q.put(start)
#     while not q.empty():
#         u = q.get()
#         print(u)
#         for v in adj.get(u, []):
#             if v not in visited:
#                 visited.add(v)
#                 q.put(v)
# graph = {1: [4, 2], 2: [3, 4], 3: [4], 4: [5]}
# bfs(graph, 1)
