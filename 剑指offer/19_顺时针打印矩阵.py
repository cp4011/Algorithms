"""输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字，例如，如果输入如下4 X 4矩阵：
            1   2   3   4
            5   6   7   8
            9   10  11  12
            13  14  15  16
则依次打印出数字1,2,3,4,8,12,16,15,14,13,9,5,6,7,11,10.
"""


# 打印并删除第一行，逆时针转动90度。重复以上步骤，直到矩阵为空。
class Solution:
    def printMatrix(self, matrix):
        s = []
        while matrix:
            s += matrix.pop(0)
            matrix = zip(*matrix)[::-1]     # 逆时针转动90度
        return s
