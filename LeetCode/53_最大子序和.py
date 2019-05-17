"""给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。
示例:
输入: [-2,1,-3,4,-1,2,1,-5,4],
输出: 6
解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。
进阶: 如果你已经实现复杂度为 O(n) 的解法，尝试使用更为精妙的分治法求解。
"""


class Solution:
    def maxSubArray(self, nums):
        """        :type nums: List[int]        :rtype: int        """
        if len(nums) == 1:
            return nums[0]
        result_sum = [0 for i in range(len(nums))]
        result_sum[0] = nums[0]
        for i in range(1, len(nums)):
            if result_sum[i - 1] < 0:
                result_sum[i] = nums[i]
            else:
                result_sum[i] = result_sum[i - 1] + nums[i]
        return max(result_sum)


print(list(map(str, [1, 2])))
print(' '.join(["1", "2"]))