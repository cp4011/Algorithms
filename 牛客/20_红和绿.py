"""牛牛有一些排成一行的正方形。每个正方形已经被染成红色或者绿色。牛牛现在可以选择任意一个正方形然后用这两种颜色的任意一种
进行染色,这个正方形的颜色将会被覆盖。牛牛的目标是在完成染色之后,每个红色R都比每个绿色G距离最左侧近。牛牛想知道他最少需要涂染几个正方形。
如样例所示: s = RGRGR
我们涂染之后变成RRRGG满足要求了,涂染的个数为2,没有比这个更好的涂染方案。
输入描述:
输入包括一个字符串s,字符串s长度length(1 ≤ length ≤ 50),其中只包括'R'或者'G',分别表示红色和绿色。
输出描述:
输出一个整数,表示牛牛最少需要涂染的正方形数量
示例1
输入
RGRGR
输出
2
"""
'''1 暴力枚举
每个位置都试一遍，假设为红与绿的分界点，在这些结果里面找到最小值。
例如对于位置i，左边全部要染成红色，右边全部要染成绿色，则当前的值为s[:i].count('G') + s[i:].count('R')。'''

s = input()
length = len(s)
num = length
for i in range(length):
    num_1 = s[:i].count("G") + s[i:].count("R")
    if num_1 < num:
        num = num_1
print(num)

# 2
s = input()
length = len(s)
num = length
count = 0
gcount = 0
for i in range(length):    # 在当前位置为R时有可能两种情况,一种是把这个位置编成G,另一种是吧前面的G全部变成R.时间复杂度O(n),空间复杂度O(1)
    if s[i] == "G":
        gcount += 1
    else:
        count = min(gcount, count+1)
print(count)


# 3  DP【注意可以没有R或没有G】
s = input()
dp = [0] * (len(s) + 1)
dp[0] = s.count('R')
for i in range(len(s)):
    if s[i] == 'G':
        dp[i+1] = dp[i] + 1
    else:
        dp[i+1] = dp[i] - 1
print(min(dp))


# 题意理解错误（不是一定要还原原来R和G的个数）
s = input()
length = len(s)
ans = 0
count = 0
for i in s:
    if i == "R":
        count += 1
for i in range(count):
    if s[i] != "R":
        ans += 1
print(2*ans)
