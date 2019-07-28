"""一个整数序列的最大连续子段和指的是从序列中选出连续的一段数字，使之和最大。
现在给定一个整数序列，你可以删除其中的连续一段（可以不删），你需要最大化删去后的最大连续字段和"""


'''最大子序和（可删除其中连续一段）
假如我们随便去掉中间的一段，则数组被分成两段（数组1，数组2）：
最大子序和 = 数组1从前往后遍历的最大子序和 + 数组2从后往前遍历的最大子序和   【相当于去掉中间一段】
'''


class Solution:
    def maxSubArray(self, nums):
        nums = [0] + nums  # 加一个0是为了防止全负数的情况,这种情况下则不包含任何元素，子序和为0
        nums1 = nums[:]
        nums1.reverse()  # 复制一份，并反转数组
        n = len(nums)
        for i in range(1, n):
            nums[i] = max(nums[i], nums[i - 1] + nums[i])  # 从前往后的最大子序和
            nums1[i] = max(nums1[i], nums1[i - 1] + nums1[i])  # 从后往前的最大子序和

        max_ = 0
        for i in range(n - 1):      # 遍历数组，找最大值
            for j in range(0, n - i - 1):
                max_ = max(max_, nums[i] + nums1[j])
        print(nums, nums1)
        return max_
