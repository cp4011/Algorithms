matrix = [
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]

matrix1 = list(map(list, zip(*matrix[::-1])))       # 顺时针旋转90度
matrix2 = list(map(list, zip(*matrix)))[::-1]       # 逆时针旋转90度

print(matrix1)
print(matrix2)


# 按照顺时针螺旋顺序，返回矩阵中的所有元素
def spiralOrder(matrix):
    ans = []
    while matrix:  # 矩阵不为空
        ans += matrix[0]
        matrix = list(map(list, zip(*matrix[1:])))[::-1]  # 删掉第一行并逆时针旋转
    return ans