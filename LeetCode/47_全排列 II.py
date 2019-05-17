"""给定一个可包含重复数字的序列，返回所有不重复的全排列。
示例:
输入: [1,1,2]
输出:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]
"""


class Solution:
    def permuteUnique(self, nums):
        answer = []
        visited = [0 for _ in range(len(nums))]     # 包含重复数字的序列，返回所有不重复的全排列

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
        return list(map(list, set([tuple(_) for _ in answer])))     # map返回的是生成器[map()],不能实现，只能list(map())

    def permuteUnique1(self, nums):
        import itertools
        return list(map(list, set(itertools.permutations(nums)))) # [list(p) for p in set(itertools.permutations(nums))]

    def permuteUnique2(self, nums):
        res, visited = [], [False] * len(nums)
        nums.sort()
        self.dfs(nums, visited, [], res)
        return res

    def dfs(self, nums, visited, path, res):
        if len(nums) == len(path):
            res.append(path)
            return
        for i in range(len(nums)):
            if not visited[i]:
                if i > 0 and not visited[i - 1] and nums[i] == nums[i - 1]:  # here should pay attention
                    continue
                visited[i] = True
                self.dfs(nums, visited, path + [nums[i]], res)
                visited[i] = False
