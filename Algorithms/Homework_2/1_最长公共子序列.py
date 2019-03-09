'''最长公共子序列
Description
给定两个字符串，返回两个字符串的最长公共子序列（不是最长公共子字符串），可能是多个。
Input
输入为两行，一行一个字符串
Output
输出如果有多个则分为多行，先后顺序不影响判断。
Sample Input 1
1A2BD3G4H56JK
23EFG4I5J6K7
Sample Output 1
23G456K
23G45JK
'''

def getLCS(str1, str2):
    length1 = len(str1)
    length2 = len(str2)
    c = [[0 for col in range(len(str2)+1)] for row in range(len(str1)+1)]
    b = [[0 for col in range(len(str2) + 1)] for row in range(len(str1) + 1)]
    # print(c)
    for i in range(1, length1+1):
        for j in range(1, length2+1):
            if str1[i-1] == str2[j-1]:
                c[i][j] = c[i-1][j-1] + 1
                b[i][j] = 2                  #2标记c[i]=c[j]的情况
            elif c[i-1][j] > c[i][j-1]:
                c[i][j] = c[i-1][j]
                b[i][j] = 1                  #1标记c[i]!=c[j] 且 max(L(s[i-1,j]),L(s[i,j-1]))前者子序列更大的情况
            elif c[i-1][j] < c[i][j-1]:
                c[i][j] = c[i][j-1]
                b[i][j] = 3                  #3标记c[i]!=c[j] 且 max(L(s[i-1,j]),L(s[i,j-1]))后者者子序列更大的情况
            else:
                c[i][j] = c[i - 1][j]
                b[i][j] = 4                  #4标记c[i]!=c[j] 且 max(L(s[i-1,j]),L(s[i,j-1]))两者相等的情况
    maxlen = c[length1][length2]
    lcs = []
    result = []
    printLCS(b, str1, lcs, result, maxlen, length1, length2)
    return result
def printLCS(b, str, lcs, result, maxlen, i, j):
    # print(lcs[::-1])
    if i == 0 or j == 0:
        # print(lcs)
        if len(lcs) == maxlen:
            if lcs[::-1] not in result:
                result.append(lcs[::-1])
        return
    if b[i][j] == 1:
        printLCS(b, str, lcs, result, maxlen, i-1, j)
    elif b[i][j] == 2:
        lcs.append(str[i - 1])
        printLCS(b, str, lcs, result, maxlen, i-1, j-1)
        lcs.pop(-1)
    elif b[i][j] == 3:
        printLCS(b, str, lcs, result, maxlen, i, j-1)
    elif b[i][j] == 4:
        printLCS(b, str, lcs, result, maxlen, i-1, j)
        printLCS(b, str, lcs, result, maxlen, i, j-1)

# str1 = "1A2BD3G4H56JK"
# str2 = "23EFG4I5J6K7"
str1 = input()
str2  = input()
result = getLCS(str1, str2)
for path in result:
    for item in path:
        print(item, end='')
    print()



# #动态规划
# str1 = input()
# str2 = input()
# dp = [[0 for j in range(len(str2) + 1)] for i in range(len(str1) + 1)]
# for i in range(1, len(str1) + 1):
#     for j in range(1, len(str2) + 1):
#         if str1[i - 1] == str2[j - 1]:
#             dp[i][j] = dp[i - 1][j - 1] + 1
#         else:
#             dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
#
# result_set = []
# lcs_str = ''
#
#
# def LCS_output(i, j, lcs_str):
#     global result_set
#     global str1
#     global str2
#     global dp
#     while (i > 0) & (j > 0):
#         if str1[i - 1] == str2[j - 1]:
#             lcs_str += str1[i - 1]
#             i -= 1
#             j -= 1
#         else:
#             if dp[i - 1][j] > dp[i][j - 1]:
#                 i -= 1
#             elif dp[i - 1][j] < dp[i][j - 1]:
#                 j -= 1
#             else:
#                 LCS_output(i - 1, j, lcs_str)
#                 LCS_output(i, j - 1, lcs_str)
#                 return
#     result_set.append(lcs_str[::-1])
#
#
# LCS_output(len(str1), len(str2), lcs_str)
#
# for line in result_set:
#     print(line)