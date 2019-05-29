"""给定一组不含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。说明：解集不能包含重复的子集。
示例:
输入: nums = [1,2,3]
输出:
[  [3],  [1],  [2],  [1,2,3],  [1,3],  [2,3],  [1,2],  []   ]
"""


class Solution:     # 一组不含重复元素的整数数组 nums，返回该数组所有可能的子集（不能包含重复的子集）
    # DFS recursively
    def subsets1(self, nums):
        res = []
        self.dfs(sorted(nums), 0, [], res)
        return res

    def dfs(self, nums, index, path, res):
        res.append(path)
        for i in range(index, len(nums)):
            self.dfs(nums, i + 1, path + [nums[i]], res)

    def subsets(self, nums):
        from itertools import combinations   # sum(iterable[, start]),start:指定相加的参数，若没有设置该值，默认为0
        #  [[()], [(1,), (2,), (3,)], [(1, 2), (1, 3), (2, 3)], [(1, 2, 3)]]
        return sum([list(combinations(nums, i)) for i in range(len(nums) + 1)], [])  # start = [],不加[],list + int(默认0)报错
        #      sum([[()], [(1,), (2,), (3,)], [(1, 2), (1, 3), (2, 3)], [(1, 2, 3)]], [])
        # 返回 [(), (1,), (2,), (3,), (1, 2), (1, 3), (2, 3), (1, 2, 3)]

    # 回溯法
    def __init__(self):
        self.result_all = None

    def subsets2(self, nums):
        self.result_all = []
        self.dfs1(nums, 0, 0, [])
        return self.result_all

    def dfs1(self, nums, n, start, result):
        self.result_all.append(result[:])
        if len(nums) == n:
            return

        for i in range(start, len(nums)):
            result.append(nums[i])
            self.dfs1(nums, n + 1, i + 1, result)
            result.pop()
        return


print(Solution().subsets([1, 2, 3]))      # [(), (1,), (2,), (3,), (1, 2), (1, 3), (2, 3), (1, 2, 3)]
'''若：return [list(combinations(nums, i)) for i in range(len(nums) + 1)] 
返回[[()], [(1,), (2,), (3,)], [(1, 2), (1, 3), (2, 3)], [(1, 2, 3)]]'''

print(sum([[()], [(1,), (2,), (3,)], [(1, 2), (1, 3), (2, 3)], [(1, 2, 3)]], []))

if (1,) in [(), (1,), (2,), (3,), (1, 2), (1, 3), (2, 3), (1, 2, 3)]:
    print("cp")