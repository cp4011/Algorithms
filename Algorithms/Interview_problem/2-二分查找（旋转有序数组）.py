"""   [0,1,2,3,4,5,6,7] might become [3,4,5,6,7,0,1,2], you will be given a target to search ,
    For example , target = 0, output will be 5 , target =10, output will be -1
"""
"""
Only three cases when we need to choose the left part (m = (left + right + 1) // 2):
left = 0, m = 3, right = 6
[4,5,6,7,0,1,2] target 5: nums[left] <= target <= nums[m]
[6,7,0,1,2,4,5] target 7: nums[m] <= nums[left] <= target
[6,7,0,1,2,4,5] target 0: target <= nums[m] <= nums[left]
"""


class Solution:
    def search(self, nums, target):                # nums: List[int], target: int
        left, right = 0, len(nums) - 1
        while left <= right:
            m = (left + right + 1) // 2
            if nums[m] == target:
                return m
            elif nums[m] <= nums[left] <= target or nums[left] <= target <= nums[m] or target <= nums[m] <= nums[left]:
                right = m - 1
            else:
                left = m + 1
        return -1


# def binary_search(alist, item):
#     """二分查找　非递归方式"""
#     n = len(alist)
#     start = 0
#     end = n-1
#     while start <= end:
#         mid = (start + end) // 2
#         if item == alist[mid]:
#             return mid
#         elif item < alist[mid]:
#             end = mid - 1
#         elif item > alist[mid]:
#             start = mid + 1
#     return False
