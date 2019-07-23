"""给定一个整数数组 nums ，找出一个序列中乘积最大的连续子序列（该序列至少包含一个数）。
示例 1:   输入: [2,3,-2,4]      输出: 6
解释:     子数组 [2,3] 有最大乘积 6。
示例 2:   输入: [-2,0,-1]       输出: 0
解释:     结果不能为 2, 因为 [-2,-1] 不是子数组。
"""
'''[2, -1, 4, -2, -3, 0, 1, 2]: 正向遍历最后得到的最大数为2 x (-1) x 4 x (-2) = 16。然而这并不是正确的结果，
最终的答案应该 反向遍历是4 x (-2) x (-3) = 24，正向/反向遍历 舍弃的是最后/第一个负数'''


class Solution:
    def maxProduct(self, nums):     # 找出一个序列中乘积最大的连续子序列（
        res = nums[0]
        temp = 1
        for i in nums:              # 正向遍历
            temp *= i
            res = max(res, temp)    # 如果当前数大于最大数，那么将最大的数替换成当前数
            if temp == 0:           # 遇到0，则将temp置为0
                temp = 1
        temp = 1
        for i in nums[::-1]:        # 反向遍历
            temp *= i
            res = max(res, temp)
            if temp == 0:
                temp = 1
        return res

    def maxProduct1(self, A):
        '''If there is no 0s in nums.
        If the number of minus nums is even, the result is the total product, can be reached from start and end of nums.
        If the number of minus nums is odd, the result can be reached from start or end of nums, split by a minus num.
        Then we can add 0s to the nums, just restart the process, set the product to itself when encounters 0.'''
        B = A[::-1]
        for i in range(1, len(A)):
            A[i] *= A[i - 1] or 1
            B[i] *= B[i - 1] or 1
        return max(A + B)


print(Solution().maxProduct([2, 3, -2, 4]))
