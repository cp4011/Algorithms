"""LeetCode 70
假设你正在爬楼梯。需要 n 阶你才能到达楼顶。每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？
注意：给定 n 是一个正整数。
示例 1：
输入： 2
输出： 2
解释： 有两种方法可以爬到楼顶。
1.  1 阶 + 1 阶
2.  2 阶
示例 2：
输入： 3
输出： 3
解释： 有三种方法可以爬到楼顶。
1.  1 阶 + 1 阶 + 1 阶
2.  1 阶 + 2 阶
3.  2 阶 + 1 阶
"""


# 非递归 （普通递归超时）      F(n) = F(n-1)+F(n-2), F(1)=1, F(2)=2
class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 3:
            return n
        else:
            i, j = 1, 2
            k = 3
            res = 0
            while k <= n:
                res = i + j
                i = j
                j = res
                k += 1
        return res


# 递归
class Solution:
    def __init__(self):
        self.map = {1: 1, 2: 2}

    def climbStairs(self, n: int) -> int:
        if n not in self.map:
            self.map[n] = self.climbStairs(n - 1) + self.climbStairs(n - 2)
        return self.map[n]

