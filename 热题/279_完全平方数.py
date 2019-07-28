"""给定正整数 n，找到若干个完全平方数（比如 1, 4, 9, 16, ...）使得它们的和等于 n。你需要让组成和的完全平方数的个数最少。
示例 1:
输入: n = 12
输出: 3
解释: 12 = 4 + 4 + 4.
示例 2:
输入: n = 13
输出: 2
解释: 13 = 4 + 9.
"""


class Solution:     # 定正整数n，找到若干个完全平方数（比如 1, 4, 9, 16, ...）使得它们的和等于 n。你需要让组成和的完全平方数的个数最少
    def numSquares(self, n):    # BFS
        """例如的13，我们要前往0，我们的第一步有两种走法，先走12和先走9。所以我们需要建立一个队列或者栈，然后将第一步的走法压入队列或者栈中。
        如下（使用队列， 我们同时记录走的步数）：（12,1），（9,1），（4,1）,我们将12出队，然后看12的下一步怎么走，发现能走11,8,3，所以我们将
        (11, 2)，(8, 2)，（3,2）入队。结果如下：（9,1），（4,1），（11,2），（8,2），（3,2）,我们将9出队，发现能走5,8，0，由于8之前已经访问过
        即使现在走8，步数也不会比之前少，所以我们将(5, 2)入队。 当访问0时，我们发现已经到达了0，那么我们更新step+1，然后出循环即可。"""
        q = []
        q.append([n, 0])
        visited = [False for _ in range(n + 1)]
        visited[n] = True

        while q:
            num, step = q.pop(0)
            i = 1
            tNum = num - i ** 2
            while tNum >= 0:
                if tNum == 0:
                    return step + 1
                if not visited[tNum]:
                    q.append([tNum, step + 1])
                    visited[tNum] = True
                i += 1
                tNum = num - i ** 2

    def numSquares1(self, n: int) -> int:    # DP方程【超时】：总和为 n 的最小完全平方数个数 = min(总和为 (n - 某个完全平方数) 的最小完全平方数个数) + 1
        dp = [0]
        for i in range(1, n+1):
            dp.append(min(dp[-j*j] for j in range(1, 1 + int(i**0.5))) + 1)
        return dp[-1]
