"""给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。
上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的高度图，在这种情况下，可以接 6 个单位的雨水（蓝色部分表示雨水）。

示例:
输入: [0,1,0,2,1,0,1,3,2,1,2,1]
输出: 6
"""

'''在一个位置能容下的雨水量 = 它左右两边柱子(包括i位置）最大高度的最小值 - 它的高度
    如 索引i为2的位置： min(1, 3) - 0 = 1
    问题就变成了: 如何找所有位置的左右两边的柱子的最大值?
    3种方法:        1. 动态规划     2. 双指针       3.栈               时间复杂度都是:O(n)
'''


class Solution:
    # 动态规划
    def trap(self, height):
        if not height: return 0
        n = len(height)
        max_left, max_right = [0] * n, [0] * n              # 注意是定义一个【数组】，记录当前索引下所遍历的最大值，而不是一个数字
        max_left[0], max_right[-1] = height[0], height[-1]  # 注意【动态规划的边界】
        for i in range(1, n):               # 找位置i左边（包括i）最大值，从所以为1（第2个）开始正向遍历
            max_left[i] = max(height[i], max_left[i-1])
        for i in range(n-2, -1, -1):        # 找位置i右边（包括i）最大值，从倒数第2个开始反向遍历
            max_right[i] = max(height[i], max_right[i+1])
        res = 0                             # 累积各位置i的容水量
        for i in range(n):
            res += min(max_left[i], max_right[i]) - height[i]   # 位置i的容水量 = 它左右两边柱子(包括i位置）最大高度的最小值 - 它的高度
        return res

    # 双指针
    def trap1(self, height):
        if not height: return 0
        left = 0
        right = len(height) - 1
        res = 0
        left_max = height[left]         # 记录左右边最大值
        right_max = height[right]
        while left < right:
            if height[left] < height[right]:
                if left_max > height[left]:
                    res += left_max - height[left]
                else:
                    left_max = height[left]
                left += 1
            else:
                if right_max > height[right]:
                    res += right_max - height[right]
                else:
                    right_max = height[right]
                right -= 1
        return res

    # 栈
    def trap2(self, height):
        if not height: return 0
        n = len(height)
        stack = []
        res = 0
        for i in range(n):
            while stack and height[stack[-1]] < height[i]:
                tmp = stack.pop()
                if not stack: break
                res += (min(height[i], height[stack[-1]]) - height[tmp]) * (i-stack[-1] - 1)
            stack.append(i)
        return res
