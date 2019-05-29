"""给出两个字符串（可能包含空格）,找出其中最长的公共连续子串,输出其长度。

输入描述:
输入为两行字符串（可能包含空格），长度均小于等于50.
输出描述:
输出为一个整数，表示最长公共连续子串的长度。

输入例子1:
abcde
abgde
输出例子1:
2
"""
'''  1. 准备一个N+1 * M+1大小的二维数组dp，置0。   2. dp[i][j]代表s1的0-i位置与s2的0-j位置中连续公共子串的最大长度。
则有：    如果s1[i] == s2[j]，dp[i][j] = dp[i-1][j-1] + 1;    否则，dp[i][j] = 0;    记录最大长度即可。'''


s1 = input()
s2 = input()
dp = [[0] * (len(s2)+1) for _ in range(len(s1)+1)]
maxl = 0
for i in range(len(s1)):
    for j in range(len(s2)):
        if s1[i] == s2[j]:
            dp[i+1][j+1] = dp[i][j] + 1
        maxl = max(maxl, dp[i+1][j+1])
print(maxl)


# 2. 按照小的字符串顺序和逆序各遍历一遍取最大值
str1 = input()
str2 = input()
if len(str1) > len(str2):
    str1, str2 = str2, str1
res = 0
start = 0
for i in range(1, len(str1) + 1):
    if str1[start:i] in str2:
        res = max(res, i - start)
    else:
        start = i
end = len(str1)
for i in range(len(str1) - 1, 0, -1):
    if str1[i:end] in str2:
        res = max(res, end - i)
    else:
        end = i
print(res)
