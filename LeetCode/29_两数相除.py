"""给定两个整数，被除数 dividend 和除数 divisor。将两数相除，要求不使用乘法、除法和 mod 运算符。
返回被除数 dividend 除以除数 divisor 得到的商。
示例 1:
输入: dividend = 10, divisor = 3
输出: 3
示例 2:
输入: dividend = 7, divisor = -3
输出: -2
说明:
被除数和除数均为 32 位有符号整数。
除数不为 0。
假设我们的环境只能存储 32 位有符号整数，其数值范围是 [−2^31,  2^31 − 1]。本题中，如果除法结果溢出，则返回 2^31 − 1。
"""


# 【除数能减去多少个被除数】单纯的-=，当被除数为2147483648，除数为 1，必然超时。可使用不断 增倍增加除数，对于较大的数，可以减少时间复杂度
# TCP/IP快恢复算法【让 -= 的值一直 temp*2 ，结果res的值也一直累加 2*i，加速进程】
class Solution:
    def divide(self, dividend, divisor):
        negetive = (dividend > 0) ^ (divisor > 0)       # 位运算符 异或^ ：相异为1    ~按位取反 &按位与 |按位或 右移>> 左移<<
        dividend, divisor = abs(dividend), abs(divisor)
        res = 0
        while dividend >= divisor:              # 输入: dividend = 8, divisor = 3     输出：2
            temp, i = divisor, 1
            while dividend >= temp:
                dividend -= temp
                res += i
                i <<= 1                         # 乘以2   注意是【左移】
                temp <<= 1                      # 乘以2
        if negetive:
            res = -res
        return min(max(-2147483648, res), 2147483647)

