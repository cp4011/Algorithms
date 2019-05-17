"""n 皇后问题研究的是如何将 n 个皇后放置在 n×n 的棋盘上，并且使皇后彼此之间不能相互攻击。
上图为 8 皇后问题的一种解法。
给定一个整数 n，返回所有不同的 n 皇后问题的解决方案。
每一种解法包含一个明确的 n 皇后问题的棋子放置方案，该方案中 'Q' 和 '.' 分别代表了皇后和空位。
示例:
输入: 4
输出: [
 [".Q..",  // 解法 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // 解法 2
  "Q...",
  "...Q",
  ".Q.."]
]
解释: 4 皇后问题存在两个不同的解法。
"""


class Solution:
    def solveNQueens(self, n):
        res = []
        self.dfs([-1] * n, 0, [], res)
        return res

    def dfs(self, nums, index, path, res):  # 填第index行的皇后位置
        """nums是一维的数组，如[1, 3, 0, 2] 表示 第1行的皇后被插入到底1列, 第二行的皇后被插入到第3列...
        index表示正在填第index行的皇后位置，从第0行开始放置皇后的列位置，每行放一个皇后，一直放到index=N-1行"""
        if index == len(nums):              # index == n时，即已经把最后一行index-1行（最后一个皇后）放置完毕，并且有效
            res.append(path)                # 将有效的n行路径path压入res中
            return                          # 回溯
        for i in range(len(nums)):          # 一列一列的遍历，从第0列开始放置皇后，并检查是否有效（与前面放置的是否有冲突）
            nums[index] = i
            if self.valid(nums, index):     # 检查第index行所放置的皇后位置是否与前面的第0,1,..index-1行是否冲突
                tmp = "." * len(nums)
                self.dfs(nums, index + 1, path + [tmp[:i] + "Q" + tmp[i + 1:]], res)

    def valid(self, nums, n):
        """检查第n行的皇后 被放置在该行的某列中，是否有效"""
        for i in range(n):
            if abs(nums[i] - nums[n]) == n - i or nums[i] == nums[n]:  # 检查是否有皇后在同一斜线上【|列之差|=|行之差|】or 同列是否有皇后
                return False
        return True
