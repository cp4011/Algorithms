"""俄罗斯方块
荧幕上一共有 n 列，每次都会有一个 1 x 1 的方块随机落下，在同一列中，后落下的方块会叠在先前的方块之上，当一整行方块都被占
满时，这一行会被消去，并得到1分。有一天，小易又开了一局游戏，当玩到第 m 个方块落下时他觉得太无聊就关掉了，小易希望你告诉
他这局游戏他获得的分数。
输入描述:
第一行两个数 n, m
第二行 m 个数，c1, c2, ... , cm ， ci 表示第 i 个方块落在第几列
其中 1 <= n, m <= 1000, 1 <= ci <= n
输出描述:
小易这局游戏获得的分数
示例1
输入
3 9
1 1 2 2 2 3 1 2 3
输出
2
"""

'''
思路： 送分题。创建一个长为n的list命名为record，遍历一遍A，
      将各个位置上加一，遍历结束后，最小值即为得分。
'''

# 读入数据
n, k = list(map(int, input().split()))
A = list(map(int, input().split()))         # A = [a1,a2,a3,...an]

record = [0 for i in range(n)]
for i in A:
    record[i - 1] += 1
print(int(min(record)))

'''小易觉得高数课太无聊了，决定睡觉。不过他对课上的一些内容挺感兴趣，所以希望你在老师讲到有趣的部分的时候叫醒他一下。
你知道了小易对一堂课每分钟知识点的感兴趣程度，并以分数量化，以及他在这堂课上每分钟是否会睡着，你可以叫醒他一次，这会使得
他在接下来的k分钟内保持清醒。你需要选择一种方案最大化小易这堂课听到的知识点分值。
输入描述:
第一行 n, k (1 <= n, k <= 105) ，表示这堂课持续多少分钟，以及叫醒小易一次使他能够保持清醒的时间。
第二行 n 个数，a1, a2, ... , an(1 <= ai <= 104) 表示小易对每分钟知识点的感兴趣评分。
第三行 n 个数，t1, t2, ... , tn 表示每分钟小易是否清醒, 1表示清醒。
输出描述:
小易这堂课听到的知识点的最大兴趣值。
示例1
输入
6 3
1 3 5 2 5 4
1 1 0 1 0 0
输出
16
'''
"""
思路：从左到右遍历，比较k长度内睡着0状态对应兴趣值的和，即叫醒一下提升的兴趣值。
    总值分为两部分：醒着的固定值 + 睡着的提升值的最大值
"""
n, k = list(map(int, input().split()))
values = list(map(int, input().split()))
awakes = list(map(int, input().split()))
base_score = 0
for i in range(n):
    if awakes[i]:
        base_score += values[i]
        values[i] = 0

max_boost_score = 0
for i in range(n):
    if not awakes[i]:
        boost_score = sum(values[i:min(i + k, n)])
        max_boost_score = max(boost_score, max_boost_score)
        # 加了下面的break语句，才使这个代码时间上终于达标
        # 扫描到距结尾不足k距离范围内的第一个睡着状态即可，后面的肯定不如这个的提升值大，没必要再跑，可提前结束
        if i > n - k + 1:
            break

score = base_score + max_boost_score
print(score)
