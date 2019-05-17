"""给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。
示例:
输入: [-2,1,-3,4,-1,2,1,-5,4],
输出: 6
解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。
"""


# 动态规划注意【初始化边界】 + 【从1开始遍历】
class Solution:
    def maxSubArray(self, nums):
        length = len(nums)
        dp = [0] * length

        dp[0] = nums[0]                                 # 【初始化边界】
        for i in range(1, length):
            dp[i] = max(nums[i], nums[i] + dp[i - 1])   # 【从1开始遍历】
        return max(dp)                                  # 注意是【max(dp),而不是dp[-1]】
