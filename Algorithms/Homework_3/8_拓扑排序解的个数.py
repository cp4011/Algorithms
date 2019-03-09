'''拓扑排序解的个数
Description
给定有向无环图中所有边，计算图的拓扑排序解的个数。
Input
输入第一行为用例个数，后面每一行表示一个图中的所有边，边的起点和终点用空格隔开，边之间使用逗号隔开。
Output
输出拓扑排序解的个数。
Sample Input 1
1
a c,b c,c d,d e,d f,e g,f g

Sample Output 1
4
'''


class Graph(object):
    def __init__(self):
        self.nodes = []
        self.edges = {}
        self.in_degree = {}

    def add_edge(self, edge):
        u, v = edge

        if u not in self.nodes:
            self.nodes.append(u)
            self.edges[u] = []
            self.in_degree[u] = 0
        if v not in self.nodes:
            self.nodes.append(v)
            self.edges[v] = []
            self.in_degree[v] = 0

        self.edges[u].append(v)
        self.in_degree[v] += 1

    def zero_in_degree_nodes(self):
        res = []
        for key, value in self.in_degree.items():
            if value == 0:
                res.append(key)
        return res

    def topology(self, order, res):
        zero_in_degree_nodes_list = self.zero_in_degree_nodes()
        if len(zero_in_degree_nodes_list) == 0:
            res.append([item for item in order])
        else:
            for node in zero_in_degree_nodes_list:
                order.append(node)
                self.in_degree.pop(node)            #dict.pop(key)      list.pop(index) 默认index = -1
                to_nodes = self.edges[node]
                for to_node in to_nodes:
                    self.in_degree[to_node] -= 1

                self.topology(order, res)

                order.pop()
                self.in_degree[node] = 0
                for to_node in to_nodes:
                    self.in_degree[to_node] += 1


num_case = int(input())
for _ in range(num_case):
    items = input().split(",")
    g = Graph()
    for item in items:
        from_node, to_node = item.split()
        g.add_edge((from_node, to_node))
    return_list = []
    g.topology([], return_list)
    print(len(return_list))


