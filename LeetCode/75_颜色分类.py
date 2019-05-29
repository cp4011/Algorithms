"""给定一个包含红色、白色和蓝色，一共 n 个元素的数组，原地对它们进行排序，使得相同颜色的元素相邻，并按照红色、白色、蓝色顺序排列。
此题中，我们使用整数 0、 1 和 2 分别表示红色、白色和蓝色。
注意:
不能使用代码库中的排序函数来解决这道题。
示例:
输入: [2,0,2,1,1,0]
输出: [0,0,1,1,2,2]
进阶：
一个直观的解决方案是使用计数排序的两趟扫描算法。首先，迭代计算出0、1 和 2 元素的个数，然后按照0、1、2的排序，重写当前数组。
你能想出一个仅使用常数空间的一趟扫描算法吗？
"""


# 时间复杂度为O(N)，空间复杂度为O(1)
class Solution:
    def sortColors(self, nums) -> None:
        ''' 荷兰三色旗问题解 ：用三个指针（p0, p2 和curr）来分别追踪0的最右边界，2的最左边界和当前考虑的元素 '''
        # 对于所有 idx < p0 : nums[idx < p0] = 0； curr是当前考虑元素的下标；对于所有 idx > p2 : nums[idx > p2] = 2
        p0 = curr = 0
        p2 = len(nums) - 1

        while curr <= p2:
            if nums[curr] == 0:     # 若 nums[curr] = 0 ：交换第 curr个 和 第p0个 元素，并将指针都向右移。
                nums[p0], nums[curr] = nums[curr], nums[p0]
                p0 += 1
                curr += 1
            elif nums[curr] == 2:   # 若 nums[curr] = 2 ：交换第 curr个和第 p2个元素，并将 p2指针左移 。
                nums[curr], nums[p2] = nums[p2], nums[curr]
                p2 -= 1
            else:                   # 若 nums[curr] = 1 ：将指针curr右移。
                curr += 1
