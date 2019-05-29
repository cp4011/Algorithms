"""编写一个高效的算法来判断 m x n 矩阵中，是否存在一个目标值。该矩阵具有如下特性：
每行中的整数从左到右按升序排列。每行的第一个整数大于前一行的最后一个整数。
示例 1:
输入:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 3
输出: true
示例 2:
输入:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 13
输出: false
"""


class Solution:
    def searchMatrix(self, matrix, target):
        if not matrix:      # 每行中的整数从左到右按升序排列。每行的第一个整数大于前一行的最后一个整数
            return False
        rows, cols = len(matrix), len(matrix[0])
        i, j = rows-1, 0                    # 从 矩阵的左下角 开始搜索
        while i >= 0 and j < cols:
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] > target:
                i -= 1
            else:
                j += 1
        return False


print(Solution().searchMatrix([
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
], 3))

