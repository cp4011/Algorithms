"""输入一个整数，输出该数二进制表示中1的个数。其中负数用补码表示。"""


class Solution:
    def NumberOf1(self, n):
        if n < 0:
            n = n & 0xffffffff
        return str(bin(n))[2:].count("1")
