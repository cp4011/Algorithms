"""现在你总共有 n 门课需要选，记为 0 到 n-1。
在选修某些课程之前需要一些先修课程。 例如，想要学习课程 0 ，你需要先完成课程 1 ，我们用一个匹配来表示他们: [0,1]
给定课程总量以及它们的先决条件，判断是否可能完成所有课程的学习？
示例 1:
输入: 2, [[1,0]]
输出: true
解释: 总共有 2 门课程。学习课程 1 之前，你需要完成课程 0。所以这是可能的。
示例 2:
输入: 2, [[1,0],[0,1]]
输出: false
解释: 总共有 2 门课程。学习课程 1 之前，你需要先完成​课程 0；并且学习课程 0 之前，你还应先完成课程 1。这是不可能的。
说明:
输入的先决条件是由边缘列表表示的图形，而不是邻接矩阵。详情请参见图的表示法。
你可以假定输入的先决条件中没有重复的边。
提示:
这个问题相当于查找一个循环是否存在于有向图中。如果存在循环，则不存在拓扑排序，因此不可能选取所有课程进行学习。
通过 DFS 进行拓扑排序 - 一个关于Coursera的精彩视频教程（21分钟），介绍拓扑排序的基本概念。
拓扑排序也可以通过 BFS 完成。
"""

"""具体做如下：
1、在开始排序前，扫描对应的存储空间（使用邻接表），将入度为 00 的结点放入队列。
2、只要队列非空，就从队首取出入度为 00 的结点，将这个结点输出到结果集中，并且将这个结点的所有邻接结点（它指向的结点）的入度减 11，在减 11 以后，如果这个被减 11 的结点的入度为 00 ，就继续入队。
3、当队列为空的时候，检查结果集中的顶点个数是否和课程数相等即可。
思考这里为什么要使用队列？（马上就会给出答案。）
在代码具体实现的时候，除了保存入度为 0 的队列，我们还需要两个辅助的数据结构：
1、邻接表：通过结点的索引，我们能够得到这个结点的后继结点；
2、入度数组：通过结点的索引，我们能够得到指向这个结点的结点个数。
这个两个数据结构在遍历题目给出的邻边以后就可以很方便地得到。"""


class Solution(object):
    # 思想：该方法的每一步总是输出当前无前趋（即入度为零）的顶点
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
        :type numCourses: int 课程门数
        :type prerequisites: List[List[int]] 课程与课程之间的关系
        :rtype: bool
        """
        # 课程的长度
        clen = len(prerequisites)
        if clen == 0:
            # 没有课程，当然可以完成课程的学习
            return True

        # 步骤1：统计每个顶点的入度
        # 入度数组，记录了指向它的结点的个数，一开始全部为 0
        in_degrees = [0 for _ in range(numCourses)]
        # 邻接表，使用散列表是为了去重
        adj = [set() for _ in range(numCourses)]

        # 想要学习课程 0 ，你需要先完成课程 1 ，我们用一个匹配来表示他们: [0,1]
        # [0, 1] 表示 1 在先，0 在后
        # 注意：邻接表存放的是后继 successor 结点的集合
        for second, first in prerequisites:
            in_degrees[second] += 1
            adj[first].add(second)

        # 步骤2：拓扑排序开始之前，先把所有入度为 0 的结点加入到一个队列中
        # 首先遍历一遍，把所有入度为 0 的结点都加入队列
        queue = []
        for i in range(numCourses):
            if in_degrees[i] == 0:
                queue.append(i)

        counter = 0
        while queue:
            top = queue.pop(0)
            counter += 1
            # 步骤3：把这个结点的所有后继结点的入度减去 1，如果发现入度为 0 ，就马上添加到队列中
            for successor in adj[top]:
                in_degrees[successor] -= 1
                if in_degrees[successor] == 0:
                    queue.append(successor)

        return counter == numCourses    # 能修的课程数 是否等于 需修的课程数