"""画家小Q又开始他的艺术创作。小Q拿出了一块有NxM像素格的画板, 画板初始状态是空白的,用'X'表示。
小Q有他独特的绘画技巧,每次小Q会选择一条斜线, 如果斜线的方向形如'/',即斜率为1,小Q会选择这条斜线中的一段格子,都涂画为蓝色,
用'B'表示;如果对角线的方向形如'\',即斜率为-1,小Q会选择这条斜线中的一段格子,都涂画为黄色,用'Y'表示。
如果一个格子既被蓝色涂画过又被黄色涂画过,那么这个格子就会变成绿色,用'G'表示。
小Q已经有想画出的作品的样子, 请你帮他计算一下他最少需要多少次操作完成这幅画。

输入描述:
每个输入包含一个测试用例。
每个测试用例的第一行包含两个正整数N和M(1 <= N, M <= 50), 表示画板的长宽。
接下来的N行包含N个长度为M的字符串, 其中包含字符'B','Y','G','X',分别表示蓝色,黄色,绿色,空白。整个表示小Q要完成的作品。

输出描述:
输出一个正整数, 表示小Q最少需要多少次操作完成绘画。

输入例子1:
4 4
YXXB
XYGX
XBYY
BXXY

输出例子1:
3

例子说明1:
XXXX
XXXX
XXXX
XXXX
->
YXXX
XYXX
XXYX
XXXY
->
YXXB
XYBX
XBYX
BXXY
->
YXXB
XYGX
XBYY
BXXY
"""


def bfs(paint, x, y, direc):
    while 0 <= x < m and 0 <= y < n:
        if direc == 1:                  # 斜线方向形如'/',即斜率为1,小Q会选择这条斜线中的一段格子,都涂画为蓝色,'B'表示
            if paint[x][y] == 'B':
                paint[x][y] = 'X'       # 消退斜线方向为'/'上的蓝色部分的格子
            elif paint[x][y] == 'G':
                paint[x][y] = 'Y'
            else:
                break
            x += 1
            y -= 1
        else:                           # 斜线方向形如'\',即斜率为-1,小Q会选择这条斜线中的一段格子,都涂画为黄色,用'Y'表示
            if paint[x][y] == 'Y':
                paint[x][y] = 'X'       # 消退斜线方向为'\'上的黄色部分的格子
            elif paint[x][y] == 'G':
                paint[x][y] = 'B'
            else:
                break
            x += 1
            y += 1

import sys
m, n = [int(x) for x in sys.stdin.readline().split()]
paint = [[x for x in sys.stdin.readline().strip()] for i in range(m)]
ans = 0
for i in range(m):                  # 依次遍历
    for j in range(n):
        if paint[i][j] == 'B':      # 蓝色格子
            ans += 1
            bfs(paint, i, j, 1)     # 消退斜线方向为'/'上的蓝色部分的格子
        elif paint[i][j] == 'Y':    # 黄色格子
            ans += 1
            bfs(paint, i, j, -1)    # 消退斜线方向为'\'上的黄色部分的格子
        elif paint[i][j] == 'G':    # 绿色格子
            ans += 2
            bfs(paint, i, j, 1)     # 消退斜线方向为'/'上的蓝色部分的格子
            bfs(paint, i, j, -1)    # 消退斜线方向为'\'上的黄色部分的格子
print(ans)
