"""给定一个整数数组 nums ，找出一个序列中乘积最大的连续子序列（该序列至少包含一个数）。
示例 1:
输入: [2,3,-2,4]
输出: 6
解释: 子数组 [2,3] 有最大乘积 6。
示例 2:
输入: [-2,0,-1]
输出: 0
解释: 结果不能为 2, 因为 [-2,-1] 不是子数组。
"""

"""本题的解题思路是同时记录当前最大值和最小值ma, mi：
当nums[i]是正数时，ma, mi * nums[i]仍然是最大值，最小值；
当nums[i]是负数时，ma, mi * nums[i]将变成最小值， 最大值；
因此，当nums[i] < 0时，我们交换ma, mi。
在遍历nums过程中，每次更新res获取全局最大值。
"""


class Solution:
    def maxProduct(self, nums):
        mi = ma = res = nums[0]
        for i in range(1, len(nums)):
            if nums[i] < 0: mi, ma = ma, mi     # 当nums[i]为负数时，交换ma, mi
            ma = max(ma * nums[i], nums[i])
            mi = min(mi * nums[i], nums[i])
            res = max(res, ma)
        return res
