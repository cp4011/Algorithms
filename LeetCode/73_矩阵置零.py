"""给定一个 m x n 的矩阵，如果一个元素为 0，则将其所在行和列的所有元素都设为 0。请使用原地算法。
示例 1:
输入:
[
  [1,1,1],
  [1,0,1],
  [1,1,1]
]
输出:
[
  [1,0,1],
  [0,0,0],
  [1,0,1]
]
示例 2:
输入:
[
  [0,1,2,0],
  [3,4,5,2],
  [1,3,1,5]
]
输出:
[
  [0,0,0,0],
  [0,4,5,0],
  [0,3,1,0]
]
进阶:
一个直接的解决方案是使用  O(mn) 的额外空间，但这并不是一个好的解决方案。
一个简单的改进方案是使用 O(m + n) 的额外空间，但这仍然不是最好的解决方案。
你能想出一个常数空间的解决方案吗？
"""

'''【常数空间复杂度】：把行列置零记录的list的功能，直接放到原来矩阵的第一行和第一列，在遍历元素的时候把需要置零的行在第一列
对应位置置零，需要置零的列在第一行对应位置置零，后续再根据第一行和第一列的标记补零。
这里存在的问题是，第一行和第一列本来存在的零和后来补上的零会混淆，原来的零具备一个功能是把第一行和第一列置零，所以在一开始
的时候，需要遍历第一行和第一列，确定是否有零。然后在最后对第一行和第一列进行置零操作。
'''
'''all(iterable) 函数用于判断给定的可迭代参数 iterable 中的所有元素是否都为 TRUE，如果是返回 True，否则返回 False。
元素除了是 0、空、None、False 外都算 True。'''


def setZeroes(matrix):
    """ Do not return anything, modify matrix in-place instead."""
    m, n, firstRowHasZero = len(matrix), len(matrix[0]), not all(matrix[0])     # 第一行元素是否含有0，返回布尔值
    for i in range(1, m):       # Use first row/column as marker, scan the matrix
        for j in range(n):
            if matrix[i][j] == 0:
                matrix[0][j] = matrix[i][0] = 0
    for i in range(1, m):       # 置0
        for j in range(n - 1, -1, -1):      # 注意此处是range(n - 1, -1, -1)
            if matrix[i][0] == 0 or matrix[0][j] == 0:
                matrix[i][j] = 0
    if firstRowHasZero:     # Set the zeros for the first row
        matrix[0] = [0] * n


""" for i in range(1, m):
            for j in range(n):
    Input    [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
    Output   [[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    Expected    [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
"""


# 更容易理解
'''【常数空间复杂度】：把行列置零记录的list的功能，直接放到原来矩阵的第一行和第一列，在遍历元素的时候把需要置零的行在第一列
对应位置置零，需要置零的列在第一行对应位置置零，后续再根据第一行和第一列的标记补零。
这里存在的问题是，第一行和第一列本来存在的零和后来补上的零会混淆，原来的零具备一个功能是把第一行和第一列置零，所以在一开始
的时候，需要遍历第一行和第一列，确定是否有零。然后在最后对第一行和第一列进行置零操作。'''
def setZeroes1(matrix):
    if not matrix or not matrix[0]:
        return
    m, n = len(matrix), len(matrix[0])
    first_row_has_zero = not all(matrix[0])     # 第一行是否有0
    first_col_has_zero = False
    for row in matrix:
        if row[0] == 0:
            first_col_has_zero = True           # 第一列是否有0
            break
    for row in range(1, m):                     # 剥去第一行和第一列，从第二行和第二列开始扫描，
        for col in range(1, n):
            if matrix[row][col] == 0:           # 若该元素为0，则在其第一行和第一列所在的位置记录
                matrix[0][col] = matrix[row][0] = 0
    for row in range(1, m):                     # 再次从第二行和第二列开始遍历
        for col in range(1, n):
            if matrix[0][col] == 0 or matrix[row][0] == 0:  # 若元素matrix[row][col]所在的位置第一行和第一列为0，则置为0
                matrix[row][col] = 0            # 置为0
    if first_row_has_zero:      # 若第一行有0，则第一行全置为0
        matrix[0] = [0] * n
    if first_col_has_zero:      # 若第一列有0，则第一列全置为0
        for row in matrix:
            row[0] = 0
