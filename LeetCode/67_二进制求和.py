"""给定两个二进制字符串，返回他们的和（用二进制表示）。输入为非空字符串且只包含数字 1 和 0。
示例 1:
输入: a = "11", b = "1"
输出: "100"
示例 2:
输入: a = "1010", b = "1011"
输出: "10101"
"""


class Solution:
    def addBinary(self, a, b):
        """        :type a: str        :type b: str        :rtype: str        """
        return bin(int(a, 2) + int(b, 2))[2:]

    """ # int(x, base=10)  x--字符串或数字, int(3.6): 返回整型数据。
        # int('12',16) 18       # 如果是带参数base的话，12要以字符串的形式进行输入，12 为 16进制，转换为10进制"""


print(bin(10)[2:])      # bin()返回str字符串类型
print(int("1010", 2))   # 转换为十进制的 返回int类型的10
