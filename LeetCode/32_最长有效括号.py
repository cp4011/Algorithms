"""给定一个只包含 '(' 和 ')' 的字符串，找出最长的包含有效括号的子串的长度。

示例 1:
输入: "(()"
输出: 2
解释: 最长有效括号子串为 "()"

示例 2:
输入: ")()())"
输出: 4
解释: 最长有效括号子串为 "()()"
"""

''' 1. 栈      时间复杂度为：O(n)
对于这种括号匹配问题，一般都是使用栈。我们先找到所有可以匹配的索引号，然后找出最长连续数列！
例如：s = )(()())，我们用栈可以找到，位置 2 和位置 3 匹配，位置 4 和位置 5 匹配，位置 1 和位置 6 匹配，
这个数组为：2,3,4,5,1,6 这是通过栈找到的,我们按递增排序！1,2,3,4,5,6，找出该数组的最长连续数列的长度就是最长有效括号长度！
所以时间复杂度来自排序：O(nlogn)，接下来我们思考，是否可以在省略排序的过程,在弹栈时候进行操作优化！
'''
class Solution(object):
    def longestValidParentheses(self, s):           # 如s = )(()())
        stack = []
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            elif stack and s[stack[-1]] == '(':
                stack.pop()
            else:
                stack.append(i)
        stack = [-1] + stack + [len(s)]             # [-1, 0, 7] 原本s的全部索引[0-6] 左右各加一个索引-1，7
        ans = 0
        for i in range(len(stack)-1):               # 若 栈stack全部匹配了，则最后的satck中只有： [-1, len(s)] 两个元素了
            ans = max(ans, stack[i+1]-stack[i]-1)   # 中间的最大间隔 即为结果，有效的括号已经在合法匹配时索引i已经弹出栈了
        return ans

    """ 2. 动态规划DP       时间复杂度：O(n)      用 dp[i] 表示以 i 结尾的最长有效括号；
        1. 当s[i] 为( , dp[i] 必然等于0,因为不可能组成有效的括号;
        2. 那么s[i] 为 )
            2.1 当 s[i-1] 为 (，那么 dp[i] = dp[i-2] + 2；
            2.2 当 s[i-1] 为 ) 并且 s[i-dp[i-1] - 1] 为 (，那么 dp[i] = dp[i-1] + 2 + dp[i-dp[i-1]-2]"""
    def longestValidParentheses1(self, s):
        n = len(s)
        if n == 0: return 0
        dp = [0] * n
        for i in range(1, n):
            if s[i] == ")":                 # s[i] 为"("时，dp[i]都为0：以该位置的索引 i 结尾的最长有效括号为0
                if s[i - 1] == "(":         # 左边第一个就是"("，直接 +2
                    dp[i] = dp[i - 2] + 2
                # 当左边第一个是 ")"，且字符串s的索引倒退 i-dp[i-1]-1 个还是有字符，且该字符为"("
                elif s[i - 1] == ")" and i - dp[i - 1] - 1 >= 0 and s[i - dp[i - 1] - 1] == "(":
                    dp[i] = dp[i - 1] + 2 + dp[i - dp[i - 1] - 2]   # 则需要另外加上dp[i-dp[i-1]-2]
        return max(dp)
