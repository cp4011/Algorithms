"""给定一个字符串 (s) 和一个字符模式 (p)。实现支持 '.' 和 '*' 的正则表达式匹配。

'.' 匹配任意单个字符。
'*' 匹配零个或多个前面的元素。
匹配应该覆盖整个字符串 (s) ，而不是部分字符串。

说明:
s 可能为空，且只包含从 a-z 的小写字母。
p 可能为空，且只包含从 a-z 的小写字母，以及字符 . 和 *。
示例 1:

输入:
s = "aa"
p = "a"
输出: false
解释: "a" 无法匹配 "aa" 整个字符串。
示例 2:

输入:
s = "aa"
p = "a*"
输出: true
解释: '*' 代表可匹配零个或多个前面的元素, 即可以匹配 'a' 。因此, 重复 'a' 一次, 字符串可变为 "aa"。
示例 3:

输入:
s = "ab"
p = ".*"
输出: true
解释: ".*" 表示可匹配零个或多个('*')任意字符('.')。
示例 4:

输入:
s = "aab"
p = "c*a*b"
输出: true
解释: 'c' 可以不被重复, 'a' 可以被重复一次。因此可以匹配字符串 "aab"。
示例 5:

输入:
s = "mississippi"
p = "mis*is*p*."
输出: false
"""


# 超时
class Solution:
    def match(self, s, pattern):
        if (len(s) == 0 and len(pattern) == 0):
            return True
        if (len(s) > 0 and len(pattern) == 0):
            return False
        if (len(pattern) > 1 and pattern[1] == '*'):
            if (len(s) > 0 and (s[0] == pattern[0] or pattern[0] == '.')):
                return (self.match(s, pattern[2:]) or self.match(s[1:], pattern[2:]) or self.match(s[1:], pattern))
            else:
                return self.match(s, pattern[2:])
        if (len(s) > 0 and (pattern[0] == '.' or pattern[0] == s[0])):
            return self.match(s[1:], pattern[1:])
        return False


# DP
class Solution(object):
    def isMatch(self, s, p):
        m, n = len(s), len(p)
        f = [[False] * (n + 1) for _ in range(2)]
        f[0][0] = True
        for j in range(2, n + 1):
            f[0][j] = p[j - 1] == '*' and f[0][j - 2]

        for i in range(1, m + 1):
            f[i % 2][0] = False
            for j in range(1, n + 1):
                if p[j - 1] != '*':
                    f[i % 2][j] = f[(i - 1) % 2][j - 1] and (s[i - 1] == p[j - 1] or p[j - 1] == '.')
                else:
                    f[i % 2][j] = f[i % 2][j - 2] or ((s[i - 1] == p[j - 2] or p[j - 2] == '.') and f[(i - 1) % 2][j])

        return f[m % 2][n]


