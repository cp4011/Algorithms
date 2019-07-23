"""给定一个正整数 n，生成一个包含 1 到 n^2 所有元素，且元素按顺时针顺序螺旋排列的正方形矩阵。
示例: 输入: 3
输出:
[
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
]
"""
'''Start with the empty matrix, add the numbers in reverse order until we added the number 1. 
Always rotate the matrix clockwise and add a top row:
    ||  =>  |9|  =>  |8|      |6 7|      |4 5|      |1 2 3|
                     |9|  =>  |9 8|  =>  |9 6|  =>  |8 9 4|
                                         |8 7|      |7 6 5|     '''


def generateMatrix(n):
    res, left = [], n*n+1
    while left > 1:
        left, right = left - len(res), left     # 第一轮res=[[]]，len(res)=1
        res = [list(range(left, right))] + list(map(list, (zip(*res[::-1]))))    # 顺时针旋转
    return res


print(generateMatrix(3))


def generateMatrix1(n):
    A = [[n*n]]
    while A[0][0] > 1:
        A = [range(A[0][0] - len(A), A[0][0])] + zip(*A[::-1])
    return A * (n>0)