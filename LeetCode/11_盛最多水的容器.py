"""给定 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点 (i, ai) 。在坐标内画 n 条垂直线，垂直线 i 的两个端点分别为
(i, ai) 和 (i, 0)。找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。
说明：你不能倾斜容器，且 n 的值至少为 2。

图中垂直线代表输入数组 [1,8,6,2,5,4,8,3,7]。在此情况下，容器能够容纳水（表示为蓝色部分）的最大值为 49。
示例:
输入: [1,8,6,2,5,4,8,3,7]
输出: 49
"""
'''双指针法 O(n)
使用两个指针，值小的指针向内移动，这样就减小了搜索空间 因为面积取决于指针的距离与值小的值乘积，如果值大的值向内移动，
距离一定减小，而求面积的另外一个乘数一定小于等于值小的值，因此面积一定减小，而我们要求最大的面积，因此值大的指针不动，
而值小的指针向内移动遍历'''


class Solution:
    def maxArea(self, height):
        res = 0
        left, right = 0, len(height)-1          # 两侧定义 双指针
        for i in range(len(height)):
            res = max(res, (right-left) * min(height[left], height[right]))
            if height[left] < height[right]:
                left += 1                       # 左指针右移
            else:
                right -= 1                      # 右指针左移
        return res


# 暴力法 O(n^2)
def maxArea1(arr):
    res = 0
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            res = max(res, (j-i)*min(arr(i), arr(j)))
    return res