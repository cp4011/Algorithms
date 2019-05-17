"""给定一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？找出所有满足条件且不重复的三元组。
注意：答案中不可以包含重复的三元组。
例如, 给定数组 nums = [-1, 0, 1, 2, -1, -4]，
满足要求的三元组集合为：
[
  [-1, 0, 1],
  [-1, -1, 2]
]
"""

''' 先排序, 然后遍历, 然后内部使用双指针, 时间复杂度应该是O(n²)  '三数之和：指针 i < l < r'
    两数之和：最小复杂度O(n)          四数字和：最小复杂度O(n**2)
'''


class Solution(object):
    def threeSum(self, nums):
        res = []
        n = len(nums)
        nums = sorted(nums)                     # 排序
        for i in range(n-2):
            if i > 0 and nums[i] == nums[i-1]:  # 避免i重复，当l的前一个和当前i位置的数相等时【说明前一轮该数字已经迭代过了】，跳过
                continue
            l, r = i+1, n-1
            new_target = -nums[i]
            while l < r:
                summ = nums[l] + nums[r]
                if summ < new_target:
                    l += 1                      # 前移一步【不能用二分查找，因为要查找多个适合的解】
                elif summ > new_target:
                    r -= 1                      # 后移一步
                else:
                    res.append([nums[i], nums[l], nums[r]])     # 插入结果
                    while l < r and nums[l+1] == nums[l]:   # 避免l重复，当l的后一个和当前l位置的数相等时，跳过l到l+1继续循环
                        l += 1
                    while r > l and nums[r-1] == nums[r]:   # 避免r重复，当l的前一个和当前r位置的数相等时，跳过r到r-1继续循环
                        r -= 1
                    l += 1
                    r -= 1
        return res
