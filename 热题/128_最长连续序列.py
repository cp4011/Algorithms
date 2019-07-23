"""给定一个未排序的整数数组，找出最长连续序列的长度。
要求算法的时间复杂度为 O(n)。
示例:
输入: [100, 4, 200, 1, 3, 2]
输出: 4
解释: 最长连续序列是 [1, 2, 3, 4]。它的长度为 4。
"""


class Solution:
    def longestConsecutive(self, nums):     # 最长连续序列（哈希表）：时间复杂度：O(n+n)  空间复杂度：O(n)
        longest_streak = 0
        num_set = set(nums)

        for num in num_set:
            if num - 1 not in num_set:  # 只有currentNum-1 不在数组 nums 里，才会开始while循环，while 循环在整个运行过程中只会被迭代 n 次
                current_num = num
                current_streak = 1

                while current_num + 1 in num_set:   # O(1)的查询
                    current_num += 1
                    current_streak += 1

                longest_streak = max(longest_streak, current_streak)

        return longest_streak

    def longestConsecutive1(self, nums):     # 排序法：时间复杂度：O(nlgn)  空间复杂度：O(1)（或者 O(n)）
        if not nums:
            return 0
        nums.sort()

        longest_streak = 1
        current_streak = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                if nums[i] == nums[i-1]+1:
                    current_streak += 1
                else:
                    longest_streak = max(longest_streak, current_streak)
                    current_streak = 1
        return max(longest_streak, current_streak)

