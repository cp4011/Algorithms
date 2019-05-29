"""假设按照升序排序的数组在预先未知的某个点上进行了旋转。( 例如，数组 [0,0,1,2,2,5,6] 可能变为 [2,5,6,0,0,1,2] )。
编写一个函数来判断给定的目标值是否存在于数组中。若存在返回 true，否则返回 false。
示例 1:
输入: nums = [2,5,6,0,0,1,2], target = 0
输出: true
示例 2:
输入: nums = [2,5,6,0,0,1,2], target = 3
输出: false
进阶:
这是 搜索旋转排序数组 的延伸题目，本题中的 nums  可能包含重复元素。
这会影响到程序的时间复杂度吗？会有怎样的影响，为什么？
"""


class Solution:
    def search(self, nums, target) -> bool:
        if not nums:
            return False
        n = len(nums)
        l, r = 0, n-1
        while l <= r:
            mid = (l + r) >> 1
            if nums[mid] == target:
                return True
            if nums[mid] < nums[l]:         # [2,5,6,0,0,1,2]
                if nums[mid] < target <= nums[r]:   # 递增区间在 [0,0,1,2]之间
                    l = mid + 1
                else:
                    r = mid - 1
            elif nums[mid] > nums[l]:       # [2,5,6,7,8,0,1,2]
                if nums[l] <= target < nums[mid]:   # 递增区间在 [2,5,6,7]之间
                    r = mid - 1
                else:
                    l = mid + 1
            elif nums[mid] == nums[l]:  # 处理边界
                l += 1
            else: r -= 1        # 此处可以省略
        return False

    # 265 / 275 通过（没处理好边界nums[mid] == nums[l]，指针l应该右移1位 l += 1）
    # """Input:[3,1], 1   Output: false   Expected: true"""
    def search1(self, nums, target) -> bool:
        if not nums:
            return False
        n = len(nums)
        l, r = 0, n-1
        while l <= r:
            mid = (l + r) >> 1
            if nums[mid] == target:
                return True
            elif nums[mid] <= nums[l]:
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
            else:
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
        return False


print(Solution().search([2, 5, 6, 0, 0, 1, 2], 3))
