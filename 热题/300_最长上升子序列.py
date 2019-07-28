"""给定一个无序的整数数组，找到其中最长上升子序列的长度。
示例:
输入: [10,9,2,5,3,7,101,18]
输出: 4
解释: 最长的上升子序列是 [2,3,7,101]，它的长度是 4。
说明:
可能会有多种最长上升子序列的组合，你只需要输出对应的长度即可。
你算法的时间复杂度应该为 O(n2) 。
进阶: 你能将算法的时间复杂度降低到 O(n log n) 吗?
"""


class Solution:
    def lengthOfLIS(self, nums):      # 贪心算法 + 二分查找[时间复杂度：O(NlogN) 空间复杂度：O(N)]
        size = len(nums)            # [10,9,2,5,3,7,101,18]
        if size < 2:                # 特判
            return size

        tail = [nums[0]]            # 为了防止后序逻辑发生数组索引越界，先把第 1 个数放进去
        for i in range(1, size):
            # 【逻辑 1】比 tail 数组实际有效的末尾的那个元素还大, 先尝试是否可以接在末尾
            if nums[i] > tail[-1]:
                tail.append(nums[i])
                continue

            # 使用二分查找法，在有序数组 tail中 找到第 1 个大于等于 nums[i] 的元素，尝试让那个元素更小
            left = 0
            right = len(tail) - 1
            while left < right:
                mid = (left + right) >> 1   # 选左中位数不是偶然，而是有原因的
                if tail[mid] < nums[i]:     # 中位数肯定不是要找的数，把它写在分支的前面
                    left = mid + 1          # 中位数肯定不是要找的数，把它写在分支的前面
                else:
                    right = mid
            # 走到这里是因为【逻辑 1】的反面，因此一定能找到第 1 个大于等于 nums[i] 的元素，因此无需再单独判断
            tail[left] = nums[i]
        return len(tail)                    # [2,4,5,6,7,12]

    # 将 dp 数组定义为：以 nums[i] 结尾的最长上升子序列的长度    那么题目要求的，就是这个 dp 数组中的最大者
    # 以数组  [10, 9, 2, 5, 3, 7, 101, 18] 为例                  dp 的值： 1  1  1  2  2  3  4    4
    def lengthOfLIS1(self, nums):    # 时间复杂度：O(N^2)，空间复杂度：O(N)
        size = len(nums)
        if size <= 1:               # 特判
            return size
        dp = [1] * size
        for i in range(1, size):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)   # 注意 + 1 的位置不要加错了
        return max(dp)              # 最后要全部一看遍，取最大值
