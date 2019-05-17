"""给定一个包括 n 个整数的数组 nums 和 一个目标值 target。找出 nums 中的三个整数，使得它们的和与 target 最接近。返回
这三个数的和。假定每组输入只存在唯一答案。
例如，给定数组 nums = [-1，2，1，-4], 和 target = 1.
与 target 最接近的三个数的和为 2. (-1 + 2 + 1 = 2).
"""

'''先排序, 然后遍历, 然后内部使用双指针, 时间复杂度应该是O(n²)'''


class Solution:
    def threeSumClosest(self, nums, target):
        if not nums:
            return
        res = nums[0] + nums[1] + nums[2]
        nums.sort()
        n = len(nums)
        for i in range(n-2):
            l, r = i+1, n-1             # 双指针       i < l < r
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if abs(res-target) > abs(s-target):     # 内置函数 abs()
                    res = s

                if s < target:
                    l += 1
                elif s > target:
                    r -= 1
                else:                                   # 如果已经等于target的话, 肯定是最接近的，直接返回
                    return s
        return res
