"""机器人走方格I
有一个XxY的网格，一个机器人只能走格点且只能向右或向下走，要从左上角走到右下角。请设计一个算法，计算机器人有多少种走法。
给定两个正整数int x,int y，请返回机器人的走法数目。保证x＋y小于等于12。
测试样例：
2,2
返回：2
"""


# 递归
def countWays(x, y):
    if x == 1 or y == 1:        # 既然是递归，再考虑退出条件：当整个矩阵只有一行 或 一列的时候只有一种走法
        return 1
    else:
        return countWays(x-1, y) + countWays(x, y-1)


# 二维数组动态规划DP，，也可以一维数组
class Robot:
    def countWays(self, x, y):
        if x == 1 or y == 1:
            return 1
        dp = [[1 for i in range(y)] for j in range(x)]
        for i in range(1, x):
            for j in range(1, y):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[-1][-1]


"""考虑原始DP问题为二维数组表示当前位置的步数，显然有: dp[i][j] = dp[i-1][j] + dp[i][j-1]，而容易发现dp数组可以压缩为
1维存储空间dp[y]。原dp[i-1][j]为上一行当前列的步数，而现dp[j]就存储了上一次该列的步数，而现dp[j-1]为左节点的步数即原dp[i][j-1]。
所以变为：dp[j] = dp[j] + dp[j-1].
"""


"""机器人走方格II
有一个XxY的网格，一个机器人只能走格点且只能向右或向下走，要从左上角走到右下角。请设计一个算法，计算机器人有多少种走法。
注意这次的网格中有些障碍点是不能走的。给定一个int[][] map(C++ 中为vector >),表示网格图，若map[i][j]为1则说明该点不是障碍
点，否则则为障碍。另外给定int x,int y，表示网格的大小。请返回机器人从(0,0)走到(x - 1,y - 1)的走法数，为了防止溢出，请将
结果Mod 1000000007。保证x和y均小于等于50
"""


class Robot:
    def countWays(self, m, x, y):
        if not m or len(m) != x or len(m[0]) != y:
            return 0
        if m[x - 1][y - 1] != 1 or m[0][0] != 1:
            return 0

        dp = [[0] * y for i in range(x)]
        dp[0][0] = 1

        for i in range(1, x):
            if m[i][0] == 1:                    # 边界上0列，没有障碍，就相等，有障碍还是为原值0
                dp[i][0] = dp[i - 1][0]
        for j in range(1, y):
            if m[0][j] == 1:
                dp[0][j] = dp[0][j - 1]

        for i in range(1, x):
            for j in range(1, y):
                if m[i][j] == 1:
                    dp[i][j] = dp[i - 1][j] % 1000000007 + dp[i][j - 1] % 1000000007

        return dp[x - 1][y - 1] % 1000000007
