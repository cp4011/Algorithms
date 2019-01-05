'''子矩阵问题
Description
给定一个矩形区域，每一个位置上都是1或0，求该矩阵中每一个位置上都是1的最大子矩形区域中的1的个数。
Input
输入的每一行是用空格隔开的0或1。
Output
输出一个数值。
Sample Input 1
1 0 1 1
1 1 1 1
1 1 1 0
Sample Output 1
6
'''

##提交版
def maxSubMatrix(matrix):
    max = 0
    sum = 0
    len_i = len(matrix)
    len_j = len(matrix[0])
    for i in range(len_i):
        for j in range(len_j):
            k = i
            v = j
            while k < len_i and int(matrix[k][j]) == 1:
                k += 1
            for index2 in range(j, len_j):
                flag = True
                for index1 in range(i, k):
                    if int(matrix[index1][index2]) == 0:
                        flag = False
                        break
                if flag == True:
                    v = index2
                else:
                    break
            sum = (k - i) * (v + 1 - j)
            if sum > max:
                max = sum
    return max

matrix = []
try:
    while True:
        s = input()
        line = s.split(' ')
        matrix.append(line)
        # line = input()
        # arr = [int(i) for i in line.split( )]
        # matrix.append(line)
except EOFError:
    pass
print(maxSubMatrix(matrix))


# matrix = []
# try:
#     while True:
#         row_input = input()
#         row_input_split = row_input.split(' ')
#         row = []
#         for item in row_input_split:
#             row.append(int(item))
#         matrix.append(row)
# except EOFError:
#     pass
# print(matrix)
# i = 0
# j = 0
# max = 0
# while i < len(matrix):
#     j = 0
#     while j < len(matrix[0]):
#         if matrix[i][j] == 0:
#             j += 1
#         else:  #  如果matrix[i][j]=0，设当前子矩阵为1*1
#             width = 1
#             height = 1
#
#             j1 = j + 1
#             while j1 < len(matrix[0]):  # 先向右扩展
#                 if matrix[i][j1] == 1:
#                     width += 1
#                 else:
#                     break
#                 j1 += 1
#
#             delta_width = 1
#             while delta_width <= width:
#                 height = 1
#                 i1 = i + 1
#                 while i1 < len(matrix):  # 再向下扩展
#                     sub_matrix = matrix[i1][j: j + delta_width]
#                     if all(sub_matrix) == 1:
#                         height += 1
#                         i1 += 1
#                     else:
#                         break
#                 sub_num = delta_width * height  # 计算当前子矩阵中1的个数
#                 if sub_num > max:
#                     max = sub_num
#
#                 delta_width += 1
#             j += 1
#     i += 1
# print(max)