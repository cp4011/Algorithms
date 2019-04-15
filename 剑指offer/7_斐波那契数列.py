"""大家都知道斐波那契数列，现在要求输入一个整数n，请你输出斐波那契数列的第n项（从0开始，第0项为0）。n<=39
"""
'F(1)=1，F(2)=1, F(n)=F(n-1)+F(n-2)（n>=3，n∈N*）'


# 递归超时，用动态规划
class Solution:
    def Fibonacci(self, n):
        if n <= 1:
            return n
        dp = [0] * (n+1)
        dp[0] = 0
        dp[1] = 1
        for i in range(2, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]
