"""给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。
你的算法时间复杂度必须是 O(log n) 级别。  如果数组中不存在目标值，返回 [-1, -1]。

示例 1:
输入: nums = [5,7,7,8,8,10], target = 8
输出: [3,4]

示例 2:
输入: nums = [5,7,7,8,8,10], target = 6
输出: [-1,-1]
"""


class Solution:
    def searchRange(self, nums, target):
        if not nums: return [-1, -1]
        n = len(nums)
        l, r = 0, n-1
        index = -1
        while l <= r:
            mid = (l+r) // 2
            if nums[mid] == target:
                index = mid
                break
            elif nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        if index == -1:
            return [-1, -1]
        i, j = index, index
        while i-1 >= 0 and nums[i-1] == target:     # 注意前后两处都是 i-1
            i -= 1
        while j+1 < n and nums[j+1] == target:
            j += 1
        return [i, j]

