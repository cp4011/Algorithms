"""有一个国家发现了5座金矿，每座金矿的黄金储量不同，需要参与挖掘的工人数也不同。参与挖矿工人的总数是10人。每座金矿要么
全挖，要么不挖，不能派出一半人挖取一半金矿。要求用程序求解出，要想得到尽可能多的黄金，应该选择挖取哪几座金矿？
1、400金/5人   2、500金/5人   3、200金/3人    4、300金/4人    5、350金/3人
"""
"""解析： N： 金矿数 ； M：人数； G[]：黄金量；   P[]：用工量；
            F(N,W)：Solution函数。
            1.最优子结构：F( 4,10 )， F( 4,10-P[4] )+G[4] )
            【解释:（前4个金矿10个工人的挖金数量）与（前4个金矿7个工人的挖金数量+第五个金矿的挖金数量）】
            2.边界：当N=1，M>=P[0]   F( N,M ) =G[0]; 当N=1，M< p[0] F(N,M)=0
            3.状态转移公式：F(5,10)=max( F(4,10), F(4,10-P[4])+G[4] ) (N>1,M>=P[N-1])
                               or   F(N,M)=F(N-1,M)   (N>1,M<P[N-1])
            解释:5个金矿10个工人的挖金数量最优选择是  第5座金矿不挖（前4个金矿10个工人的挖金数量）与
                                      第5座金矿要挖（前4个金矿7个工人的挖金数量+第五个金矿的挖金数量）的较大值。(防止减出负数)
"""
import copy


def good(n, w, g=[], p=[]):             # n为金矿数，w为人数，g为金矿数组，p为人数数组
    arr = [0] * w                       # 保存上一行结果的数组
    for j in range(w):
        if (j + 1) >= p[0]:             # i为坐标， i+1为人数
            arr[j] = g[0]
    res = copy.copy(arr)                # 保存保存返回结果的数组，浅拷贝或深copy都可以
    print(res)                          # 只有一座金矿的情况（填充表格的第一行）

    for i in range(1, n):               # 外层循环为金矿数量（表格从第二座金矿开始，即填充表格的第二行）
        for j in range(w):              # 内层循环为旷工数量
            if (j + 1) < p[i]:          # j为坐标， j+1为人数
                arr[j] = res[j]         # 此条件下，和上一行表格的结果相同
            else:                       # j+1 >= p[i]
                t = 0 if ((j+1 - p[i]) - 1) < 0 else j - p[i]   # 防止负数取到后面的值【-1：因为数组下标要-1】【j+1 - p[i] - 1  = -1 代表：人数刚刚够挖地i座矿，没有剩余的人；等于0则说明还多出一个人了】
                arr[j] = max(res[j], res[t] + g[i])   # 挖和不挖第i座金矿中取最大者【res[t]+g[i]为挖第i座金矿,res[已有人数 - 第i座所需人数]+第i座金子g[i]】
        res = copy.copy(arr)            # 更新结果数组，浅拷贝或深copy都可以
        print(res)
    return res.pop()                    # 返回挖n座金矿的最大收益


if __name__ == '__main__':
    res = good(5, 10, [400, 500, 200, 300, 350], [5, 5, 3, 4, 3])
    print(res)


# 自顶向下简单递归：时间空间：O(2^N) 与M无关
class Solution1:
    def __init__(self, G=[], P=[]):
        self.G = G
        self.P = P
        self.N = len(self.G)

    def GoldMining(self, N, M):                     # 金矿数量N，人数M; 黄金量列表G， 用工量列表P；
        if N == 1 and M >= self.P[0]:               # 定义边界
            return self.G[0]
        if N == 1 and 0 <= M < self.P[0]:
            return 0
        if N > 1 and M >= self.P[N-1]:              # 定义状态转移 两种情况
            return max(self.GoldMining(N-1, M), self.GoldMining(N-1, M-self.P[N-1])+self.G[N-1])
        if N > 1 and M < self.P[N-1]:
            return self.GoldMining(N-1, M)
