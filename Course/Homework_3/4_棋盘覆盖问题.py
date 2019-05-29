'''棋盘覆盖问题
Description
棋盘覆盖问题：给定一个大小为2^n2^n个小方格的棋盘，其中有一个位置已经被填充，现在要用一个L型（22个小方格组成的大方格中去掉
其中一个小方格）形状去覆盖剩下的小方格。求出覆盖方案，即哪些坐标下的小方格使用同一个L型格子覆盖。注意：坐标从0开始。
左上方的第一个格子坐标为(0,0)，第一行第二个坐标为(0,1)，第二行第一个为(1,0)，以此类推。
Input
输入第一行为测试用例个数，后面每一个用例有两行，第一行为n值和特殊的格子的坐标（用空格隔开），第二行为需要查找其属于同一个L型格子的格子坐标。
Output
输出每一行为一个用例的解，先按照行值从小到大、再按照列值从小到大的顺序输出每一个用例的两个坐标；用逗号隔开。
Sample Input 1
1
1 1 1
0 0
Sample Output 1
0 1,1 0
'''


import math
def setL(x, y, xx, yy, length):
    global flag
    global t
    if length == 1:
        return
    t += 1
    tem = t
    l = length // 2
    if xx < x + l and yy < y + l:   # 特殊点在左上方
        setL(x, y, xx, yy, l)
    else:
        flag[x + l - 1][y + l - 1] = tem
        setL(x, y, x+l-1, y+l-1, l)

    if xx >= x + l and yy < y + l:   # 特殊点在左下方
        setL(x+l, y, xx, yy, l)
    else:
        flag[x + l][y + l - 1] = tem
        setL(x+l, y, x+l, y+l-1, l)

    if xx < x + l and yy >= y + l:   # 特殊点在右上方
        setL(x, y+l, xx, yy, l)
    else:
        flag[x + l - 1][y + l] = tem
        setL(x, y+l, x+l-1, y+l, l)

    if xx >= x + l and yy >= y + l:   # 特殊点在右下方
        setL(x+l, y+l, xx, yy, l)
    else:
        flag[x + l][y + l] = tem
        setL(x+l, y+l, x+l, y+l, l)


num = int(input())
for i in range(num):
    line1 = [int(item) for item in input().split(' ')]
    line2 = [int(item) for item in input().split(' ')]
    n = line1[0]
    length = int(math.pow(2, n))
    special_x = line1[1]
    special_y = line1[2]
    find_x = line2[0]
    find_y = line2[1]
    flag = [[0 for i in range(length)] for j in range(length)]
    t = 0
    setL(0, 0, special_x, special_y, length)
    f = flag[find_x][find_y]
    count = 0
    i = 0
    while i < length:
        j = 0
        while j < length:
            if (flag[i][j] == f) and not (i == find_x and j == find_y):
                count += 1
                if count == 1:
                    print(i, j, end=',')
                else:
                    print(i, j)
            j += 1
        i += 1


# def chess(tr, tc, pr, pc, size):
#     global mark
#     global table
#     mark += 1
#     count = mark
#     if size == 1:
#         return
#     half = size // 2
#     if pr < tr + half and pc < tc + half:
#         chess(tr, tc, pr, pc, half)
#     else:
#         table[tr + half - 1][tc + half - 1] = count
#         chess(tr, tc, tr + half - 1, tc + half - 1, half)
#     if pr < tr + half and pc >= tc + half:
#         chess(tr, tc + half, pr, pc, half)
#     else:
#         table[tr + half - 1][tc + half] = count
#         chess(tr, tc + half, tr + half - 1, tc + half, half)
#     if pr >= tr + half and pc < tc + half:
#         chess(tr + half, tc, pr, pc, half)
#     else:
#         table[tr + half][tc + half - 1] = count
#         chess(tr + half, tc, tr + half, tc + half - 1, half)
#     if pr >= tr + half and pc >= tc + half:
#         chess(tr + half, tc + half, pr, pc, half)
#     else:
#         table[tr + half][tc + half] = count
#         chess(tr + half, tc + half, tr + half, tc + half, half)
#
#
# def show(table):
#     n = len(table)
#     for i in range(n):
#         for j in range(n):
#             print(table[i][j], end='   ')
#         print('')
#
#
# N = int(input())
# while N > 0:
#     arr = list(map(int, input().split()))
#     k = arr[0]
#     tx = arr[1]
#     ty = arr[2]
#     x, y = map(int, input().split())
#
#     r = []
#     n = 2**k
#     mark = 0
#     table = [[-1 for x in range(n)] for y in range(n)]
#     chess(0, 0, tx, ty, n)
#     # show(table)
#
#     flag = table[x][y]
#     # print(flag)
#     for i in range(n):
#         for j in range(n):
#             if table[i][j] == flag:
#                 s = str(i)+" "+str(j)
#                 if s != str(x)+" "+str(y):
#                     r.append(s)
#     print(','.join(r))
#     N = N-1



