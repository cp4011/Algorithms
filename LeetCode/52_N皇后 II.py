"""n 皇后问题研究的是如何将 n 个皇后放置在 n×n 的棋盘上，并且使皇后彼此之间不能相互攻击。上图为 8 皇后问题的一种解法。
给定一个整数 n，返回 n 皇后不同的解决方案的数量。
示例:
输入: 4
输出: 2
解释: 4 皇后问题存在如下两个不同的解法。
[
 [".Q..",  // 解法 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // 解法 2
  "Q...",
  "...Q",
  ".Q.."]
]
"""
'''返回 n 皇后不同的解决方案的数量：与N皇后一样，只是不需要记录路径path'''


class Solution:
    def totalNQueens(self, n):
        self.res = 0                # 返回的值是个数字，不是一个list，可用全局变量去记录结果
        self.dfs([-1] * n, 0)
        return self.res

    def dfs(self, nums, index):
        if index == len(nums):
            self.res += 1           # 不用记录path，res的接发数量+1
            return
        for i in range(len(nums)):
            nums[index] = i
            if self.valid(nums, index):
                self.dfs(nums, index + 1)

    def valid(self, nums, n):
        for i in range(n):
            if nums[i] == nums[n] or abs(nums[n] - nums[i]) == n - i:
                return False
        return True