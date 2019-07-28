"""给定长度为 n 的整数数组 nums，其中 n > 1，返回输出数组 output ，其中 output[i] 等于 nums 中除 nums[i] 之外
其余各元素的乘积。
示例:
输入: [1,2,3,4]
输出: [24,12,8,6]
说明: 请不要使用除法，且在 O(n) 时间复杂度内完成此题。
进阶：
你可以在常数空间复杂度内完成这个题目吗？（ 出于对空间复杂度分析的目的，输出数组不被视为额外空间。）
"""


class Solution:
    def productExceptSelf(self, nums: [int]) -> [int]:
        res, p, q = [1], 1, 1   # res第一个元素为1
        for i in range(len(nums) - 1):  # 正向遍历（正向累乘元素）
            p *= nums[i]        # 累乘
            res.append(p)       # 在元素1后面，继续append正向累乘的q
        for i in range(len(nums) - 1, 0, -1):    # 反向遍历（反向累乘元素）
            q *= nums[i]
            res[i - 1] *= q     # 此时nums[i-1]可被认为是1
        return res              # res数组中各元素是存着 除自身以外数组的乘积
