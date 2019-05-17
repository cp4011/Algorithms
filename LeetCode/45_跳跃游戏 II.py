"""给定一个非负整数数组，你最初位于数组的第一个位置。数组中的每个元素代表你在该位置可以跳跃的最大长度。
你的目标是使用最少的跳跃次数到达数组的最后一个位置。
示例:
输入: [2,3,1,1,4]
输出: 2
解释: 跳到最后一个位置的最小跳跃数是 2。
     从下标为 0 跳到下标为 1 的位置，跳 1 步，然后跳 3 步到达数组的最后一个位置。
说明: 假设你总是可以到达数组的最后一个位置。
"""


class Solution:
    def jump(self, nums):
        if len(nums) <= 1:                  # 输入：[0]
            return 0
        start, end = 0, 0 + nums[0]         # 最初位于数组的第一个位置索引0，定义两个指针，表示这一轮可以到达的范围
        max_dis = 0 + nums[0]               # 记录遍历过程中max下一轮可以到达的最远节点i + nums[i]
        step = 1
        while end < len(nums) - 1:          # 不满足该条件时：说明更新后的end已经大于等于最后一个位置的索引
            for i in range(start + 1, end + 1):
                max_dis = max(max_dis, i + nums[i])     # 记录下一轮可到达的最大值 【索引+索引位置的值 i + nums[i] 】
            start, end = end, max_dis       # 更新下一轮的参数
            step += 1
        return step
