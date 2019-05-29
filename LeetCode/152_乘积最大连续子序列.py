"""给定一个整数数组 nums ，找出一个序列中乘积最大的连续子序列（该序列至少包含一个数）。
示例 1:
输入: [2,3,-2,4]
输出: 6
解释: 子数组 [2,3] 有最大乘积 6。
示例 2:
输入: [-2,0,-1]
输出: 0
解释: 结果不能为 2, 因为 [-2,-1] 不是子数组。
"""
'''If there is no 0s in nums.
If the number of minus nums is even, the result is the total product, can be reached from start and end of nums.
If the number of minus nums is odd, the result can be reached from start or end of nums, split by a minus num.
Then we can add 0s to the nums, just restart the process, set the product to itself when encounters 0.'''


class Solution:
    def maxProduct(self, A):
        B = A[::-1]
        for i in range(1, len(A)):
            A[i] *= A[i - 1] or 1
            B[i] *= B[i - 1] or 1
        return max(A + B)

    def maxProduct1(self, nums):
        '''类似于动态规划思想，一次遍历，每一步的中间变量表示当前位置的最大正值和负值，对长度大于1的结果必定是大于0的，所以
        当前位置连续乘积最大值小于0或最小值大于0时都令成0即可，比较res和当前最大正值即可。'''
        res = nums[0]
        if nums[0] >= 0:
            mid = [0, nums[0]]
        else:
            mid = [nums[0], 0]
        for i in range(1, len(nums)):
            if nums[i] >= 0:
                mid[1] = max(nums[i], nums[i]*mid[1])
                mid[0] = mid[0]*nums[i]
            else:
                mid[0], mid[1] = min(nums[i], nums[i]*mid[1]), nums[i]*mid[0]
            res = max(res, mid[1])
        return res


print(Solution().maxProduct([2, 3, -2, 4]))
