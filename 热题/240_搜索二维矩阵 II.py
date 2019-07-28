"""编写一个高效的算法来搜索 m x n 矩阵 matrix 中的一个目标值 target。该矩阵具有以下特性：
        每行的元素从左到右升序排列。每列的元素从上到下升序排列。
示例:  现有矩阵 matrix 如下：
[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
给定 target = 5，返回 true。
给定 target = 20，返回 false。
"""


class Solution:
    def searchMatrix(self, matrix, target):     # 时间复杂度O(n+m),行只能减少m次，而列只能增加n次,因此导致while循环终止之前，循环不能运行超过n+m次 空间复杂度O(1)
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False
        height = len(matrix)
        width = len(matrix[0])
        row = height - 1
        col = 0
        while col < width and row >= 0:
            if matrix[row][col] > target:
                row -= 1
            elif matrix[row][col] < target:
                col += 1
            else:  # found it
                return True
        return False
