"""一条包含字母 A-Z 的消息通过以下方式进行了编码：
'A' -> 1
'B' -> 2
...
'Z' -> 26
给定一个只包含数字的非空字符串，请计算解码方法的总数。

示例 1:

输入: "12"
输出: 2
解释: 它可以解码为 "AB"（1 2）或者 "L"（12）。
示例 2:

输入: "226"
输出: 3
解释: 它可以解码为 "BZ" (2 26), "VF" (22 6), 或者 "BBF" (2 2 6) 。
"""

'''状态转移方程是 dp[n] = dp[n - 1] + dp[n - 2], 注意一下0和超过26的约束'''


class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == '0':
            return 0
        length = len(s)
        dp = [1] * length                               # 初始化第一个值为1 【边界】
        for i in range(1, length):                      # 从1开始遍历
            if s[i] == '0':
                if s[i - 1] == '1' or s[i - 1] == '2':      # i位置为'0'且前一个字符为'1'或'2'，dp[i] = dp[i - 2]
                    dp[i] = dp[i - 2] if i - 2 >= 0 else 1
                else:
                    return 0
            elif s[i] <= '6':                               # i位置为'1-6'
                dp[i] = dp[i - 1]                           # 且前一个字符是'3-9'
                if s[i - 1] == '1' or s[i - 1] == '2':
                    dp[i] += (dp[i - 2] if i - 2 >= 0 else 1)   # 当前一个字符是'1'或'2'时，还要加上dp[i-2]
            else:                                           # i位置为'7-9'
                dp[i] = dp[i - 1]                           # 且前一个字符是'2-9'
                if s[i - 1] == '1':                         # 当前一个字符是'1'时，还要加上dp[i-2]
                    dp[i] += (dp[i - 2] if i - 2 >= 0 else 1)

        return dp[-1]

