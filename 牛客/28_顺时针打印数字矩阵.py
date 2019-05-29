"""给定一个数字矩阵，请设计一个算法从左上角开始顺时针打印矩阵元素
输入描述:
输入第一行是两个数字，分别代表行数M和列数N；接下来是M行，每行N个数字，表示这个矩阵的所有元素；当读到M=-1，N=-1时，输入终止。
输出描述:
请按逗号分割顺时针打印矩阵元素（注意最后一个元素末尾不要有逗号！例如输出“1，2，3”，而不是“1，2，
3，”），每个矩阵输出完成后记得换行
输入例子1:
3 3
1 2 3
4 5 6
7 8 9
-1 -1
输出例子1:
1,2,3,6,9,8,7,4,5
"""
'''     list(zip(*mat[::-1]))        # 矩阵 顺时针旋转90度
        list(zip(*mat))[::-1]        # 矩阵 逆时针旋转90度
'''





# 93.33%
def func(mat):
    ans = []
    while len(mat) > 0:
        ans += mat[0]                               # 将矩阵的首行放入 ret
        mat = list(reversed(list(zip(*mat[1:]))))   # 去掉矩阵首行后逆时针旋转90度   mat = [x for x in zip(*mat[1:])][::-1]
    return ans


while True:
    n, m = [int(i) for i in input().split()]
    if n == -1 and m == -1:
        break
    mat = []
    for i in range(n):
        mat.append([int(i) for i in input().split()])
    ans = map(str, func(mat))
    print(",".join(ans))


'''思路：先取矩阵的第一行，接着将剩下作为新矩阵进行一个逆时针90度的翻转，接着获取第一行，直到矩阵为空。'''


def printMatrix(matrix):
    result = []
    while matrix:
        result += matrix.pop(0)
        if not matrix or not matrix[0]:
            break
        matrix = turn(matrix)
    print(result)


def turn(matrix):
    nrow = len(matrix)
    ncol = len(matrix[0])
    newMatrix = []
    for i in range(ncol):
        temp = []
        for j in range(nrow):
            temp.append(matrix[j][i])
        newMatrix.append(temp)
    newMatrix.reverse()
    return newMatrix
