"""给定两个整数 n 和 k，返回 1 ... n 中所有可能的 k 个数的组合。
示例:
输入: n = 4, k = 2
输出:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]
"""


class Solution:
    def combine(self, n, k):        # 给定两个整数 n 和 k，返回 1 ... n 中所有可能的 k 个数的组合。
        from itertools import combinations
        return list(combinations(list(range(1, n + 1)), k))

    # 回溯法
    def combine1(self, n, k):
        def backtrack(first=1, curr=[]):
            if len(curr) == k:              # 若组合已经完成
                output.append(curr[:])      # 【注意此处是curr[:]，是curr的拷贝
            for i in range(first, n + 1):
                curr.append(i)              # 将i加入当前组合中
                backtrack(i + 1, curr)      # 用下一个整数去完成组合
                curr.pop()                  # 回溯

        output = []
        backtrack()                         # 由于有默认参数，相当于backtrack(1, [])
        return output

