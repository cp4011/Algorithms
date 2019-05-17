"""给定一个没有重复数字的序列，返回其所有可能的全排列。
示例:
输入: [1,2,3]
输出:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
"""


class Solution:
    def permute(self, nums):            # 没有重复数字的序列，返回其所有可能的全排列
        answer = []
        visited = [0 for _ in range(len(nums))]
        def dfs(ans):
            if len(ans) == len(nums):
                answer.append(ans[:])
                return
            for i in range(len(nums)):
                if visited[i] != 1:
                    visited[i] = 1
                    dfs(ans + [nums[i]])
                    visited[i] = 0
        dfs([])
        return answer

    def permute1(self, nums):
        import itertools
        return list(map(list, itertools.permutations(nums)))

    def permute2(self, nums):
        res = []
        self.dfs(nums, [], res)
        return res

    def dfs(self, nums, path, res):
        if not nums:
            res.append(path)
        for i in range(len(nums)):      # 回溯
            self.dfs(nums[:i] + nums[i + 1:], path + [nums[i]], res)


# 将任意数字作为第一个数字，并附加其他数字的任何排列
def permute(nums):
    return [[n] + p for i, n in enumerate(nums) for p in permute(nums[:i] + nums[i+1:])] or [[]]
