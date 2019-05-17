"""给定一个 n × n 的二维矩阵表示一个图像。  将图像顺时针旋转 90 度。
说明：
你必须在原地旋转图像，这意味着你需要直接修改输入的二维矩阵。请不要使用另一个矩阵来旋转图像。
示例 1:
给定 matrix =
[
  [1,2,3],
  [4,5,6],
  [7,8,9]
],
原地旋转输入矩阵，使其变为:
[
  [7,4,1],
  [8,5,2],
  [9,6,3]
]

示例 2:
给定 matrix =
[
  [ 5, 1, 9,11],
  [ 2, 4, 8,10],
  [13, 3, 6, 7],
  [15,14,12,16]
],
原地旋转输入矩阵，使其变为:
[
  [15,13, 2, 5],
  [14, 3, 4, 1],
  [12, 6, 8, 9],
  [16, 7,10,11]
]
"""


class Solution:
    def rotate(self, matrix):
        """ 不返回，原地修改matrix """
        for i in range(len(matrix)):
            for j in range(i+1, len(matrix)):   # 沿着对角线，镜像反转
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        for l in matrix:                        # 将matrix中的 各元素列表l中的元素 反转
            l.reverse()

    def rotate1(self, matrix):
        matrix[:] = list(map(list, zip(*matrix[::-1])))

    def rotate2(self, matrix):
        """归纳法，发现规律： [x][y] --> [y][n - 1 - x]      自外向内顺时针循环
        自外向内一共有不超过n/2层（单个中心元素不算一层）矩形框。对于第times层矩形框，其框边长len=nums-(times/2)，将其顺时针
        分为4份len-1的边，对四条边进行元素的循环交换即可。"""
        n = len(matrix)
        for l in range(n // 2):             # 自外向内一共有不超过n/2层矩形框（单个中心元素不算一层， 不需旋转）
            r = n - 1 - l
            for p in range(l, r):
                q = n - 1 - p
                cache = matrix[l][p]
                matrix[l][p] = matrix[q][l]
                matrix[q][l] = matrix[r][q]
                matrix[r][q] = matrix[p][r]
                matrix[p][r] = cache
