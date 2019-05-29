"""给定一个仅包含 0 和 1 的二维二进制矩阵，找出只包含 1 的最大矩形，并返回其面积。
示例:
输入:
[
  ["1","0","1","0","0"],
  ["1","0","1","1","1"],
  ["1","1","1","1","1"],
  ["1","0","0","1","0"]
]
输出: 6
"""
'''基于84题： 遍历每一行，在垂直方向进行（连续的1）相加，变成一维数组，利用84题的解法进行求解最大值'''
def maximalRectangle(matrix):
    if not matrix or not matrix[0]:
        return 0
    n = len(matrix[0])
    height = [0] * (n + 1)  # n+1列，最后一列为0
    ans = 0
    for row in matrix:      # 遍历4行数组
        for i in range(n):      # height[1,0,1,0,0],  [2,0,2,1,1]     [3,1,3,2,2]     [4,0,0,3,0]每个列表中最后还要添加一个0
            height[i] = height[i] + 1 if row[i] == '1' else 0
        stack = [-1]        # 定义单增栈，存储单增height元素的索引
        for i in range(n + 1):  # 遍历数组height中的n+1列
            while height[i] < height[stack[-1]]:    # 不满足单增元素（将大于 索引i位置的元素 的所有元素的索引都弹出，并计算面积
                h = height[stack.pop()]     # 弹出栈顶最大元素
                w = i - 1 - stack[-1]       # 索引相减，求矩形宽度
                ans = max(ans, h * w)       # 记录当前最大矩形面积
            stack.append(i)     # 将索引i压入单增栈
    return ans      # 前三行所得的 height为[3,1,3,2,2]时，遍历height数组每一列时，得到最大矩形面积
