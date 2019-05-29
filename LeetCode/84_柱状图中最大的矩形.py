"""给定 n 个非负整数，用来表示柱状图中各个柱子的高度。每个柱子彼此相邻，且宽度为 1 。
求在该柱状图中，能够勾勒出来的矩形的最大面积。
以上是柱状图的示例，其中每个柱子的宽度为 1，给定的高度为 [2,1,5,6,2,3]。
图中阴影部分为所能勾勒出的最大矩形面积，其面积为 10 个单位。
示例:
输入: [2,1,5,6,2,3]
输出: 10      【5和6 形成的最大矩形面积是 5*2 = 10】
"""
'''直方图形面积要最大的话，需要尽可能的使用连续的矩形多，并且最低一块的高度要高。用单调栈来做，首先要考虑用递增栈，
还是用递减栈。增栈是维护递增的顺序，当遇到小于栈顶元素的数就开始处理，而递减栈正好相反，维护递减的顺序，当遇到大于
栈顶元素的数开始处理。此题我们需要按从高板子到低板子的顺序处理，先处理最高的板子，宽度为1，然后再处理
旁边矮一些的板子，此时长度为2，因为之前的高板子可组成矮板子的矩形 ，因此我们需要一个递增栈，当遇到大的数字直接进栈，而
当遇到小于栈顶元素的数字时，就要取出栈顶元素进行处理了，那取出的顺序就是从高板子到矮板子了，于是乎遇到的较小的数字只是
一个触发，表示现在需要开始计算矩形面积了，为了使得最后一块板子也被处理，在高度数组最后面加上一个0，
这样原先的最后一个板子也可以被处理了。由于栈顶元素是矩形的高度，那么关键就是求出来宽度，那么跟之前那道Trapping Rain Water
一样，单调栈中不能放高度，而是需要放坐标。由于我们先取出栈中最高的板子，那么就可以先算出长度为1的矩形面积了，然后再取
下一个板子，此时根据矮板子的高度算长度为2的矩形面积，以此类推，知道数字大于栈顶元素为止，再次进栈!  【单调栈】
'''
""" input [2,1,5,6,2,3] ;(i, h, w) change:  (1, 2, 1)  (4, 6, 1)  (4, 5, 2)得到5*2=10  (6, 3, 1)  (6, 2, 4)  (6, 1, 6)"""


def largestRectangleArea(height):
    height.append(0)        # 在所有柱状图高度后面加上一高度为0的栏，让前面所有剩余没处理的栏得到处理(height是n个非负整数)
    stack = [-1]            # 定义单调栈（单增栈），存储递增元素 height的索引
    ans = 0
    for i in range(len(height)):
        while height[i] < height[stack[-1]]:    # 当前遍历到的索引i位置的height小于栈顶元素，即不满足递增了，触发面积计算
            h = height[stack.pop()]  # 弹出单增栈中栈顶元素为高度h，h记录着while循环中一直弹出的栈顶元素，h一直在减小，但w在增加
            w = i - 1 - stack[-1]    # 计算矩形宽度w，i-1是矩形右边界所在的索引，在一轮while循环中不变，改变的是左边界一直在左移，高度同时也在减小
            ans = max(ans, h * w)    # 记录当前最大矩形面积
        stack.append(i)
    height.pop()
    return ans


