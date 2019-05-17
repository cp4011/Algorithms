"""假设按照升序排序的数组在预先未知的某个点上进行了旋转。( 例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] )。
搜索一个给定的目标值，如果数组中存在这个目标值，则返回它的索引，否则返回 -1 。
你可以假设数组中不存在重复的元素。你的算法时间复杂度必须是 O(log n) 级别。

示例 1:
输入: nums = [4,5,6,7,0,1,2], target = 0
输出: 4

示例 2:
输入: nums = [4,5,6,7,0,1,2], target = 3
输出: -1
"""


'''直接使用二分法，判断旋转的位置以及target的位置：
    1. mid直接等于target
    2. mid的左半边是递增区域
        a. target 在 left 和 mid 之间，则r指针左移
        b. 不在之间，则l指针右移
    3. mid的右半边是递增区域    
        a. target 在 mid 和 right 之间  ，则l指针右移
        b. 不在之间，则r指针左移
'''
class Solution:
    def search(self, nums, target):
        if not nums:
            return -1
        n = len(nums)
        l, r = 0, n-1
        while l <= r:
            mid = (l+r) // 2                # 考虑(l+r+1) // 2   注意特殊输入：[3,1]，1
            if nums[mid] == target:
                return mid
            if nums[mid] >= nums[l]:        # mid的左侧是递增区间   注意此处的等于是针对 l=mid， 注意特殊输入：[3,1]，1
                if nums[l] <= target < nums[mid]:   # 再来考虑 target 是否在左侧的递增区间，如果是，这r指针左移
                    r = mid - 1
                else:
                    l = mid + 1
            else:                           # mid的右侧侧是递增区间
                if nums[mid] < target <= nums[r]:   # 再来考虑 target 是否在右侧的递增区间，如果是，这l指针右移
                    l = mid + 1
                else:
                    r = mid - 1
        return -1

    def search1(self, nums, target):
        lo, hi = 0, len(nums) - 1
        while lo < hi:
            mid = (lo + hi) / 2
            if (nums[0] > target) ^ (nums[0] > nums[mid]) ^ (target > nums[mid]):
                lo = mid + 1
            else:
                hi = mid
        return lo if target in nums[lo:lo + 1] else -1
