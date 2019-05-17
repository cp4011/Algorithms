"""实现 pow(x, n) ，即计算 x 的 n 次幂函数。
示例 1:
输入: 2.00000, 10
输出: 1024.00000
示例 2:
输入: 2.10000, 3
输出: 9.26100
示例 3:
输入: 2.00000, -2
输出: 0.25000
解释: 2^-2 = 1/2^2 = 1/4 = 0.25
说明: -100.0 < x < 100.0  n 是 32 位有符号整数，其数值范围是 [−2^31, 2^31 − 1] 。
"""


# return x ** n
class Solution:
    # 迭代
    def myPow(self, x, n):
        if n < 0:
            x = 1 / x
            n = -n
        pow = 1
        while n:
            if n & 1:   # n是奇数，n&1 位运算(按位与)：可判断n是否为奇数，偶数时n&1返回0；奇数时返回1。
                pow *= x
            x *= x
            n >>= 1     # 【右移一位 相当于 地板除以2】 //2 , 【注意不是 >>=1 是1，右移1位】
        return pow

    # 循环
    def myPow1(self, x, n):
        if not n:                               # 注意是对 n
            return 1
        if n < 0:
            return 1 / self.myPow(x, -n)        # 1/ 放在外面
        if n & 1:                               # 如果n为奇数
            return x * self.myPow(x, n-1)       # 注意 x* 在外面。对外面整体
        return self.myPow(x*x, n//2)            # 注意 x* 在里面，n必须是地板除 【n//2 相当于 n>>1】
