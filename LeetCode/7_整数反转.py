"""给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。
示例 1:
输入: 123
输出: 321

 示例 2:
输入: -123
输出: -321

示例 3:
输入: 120
输出: 21
注意:
假设我们的环境只能存储得下 32 位的有符号整数，则其数值范围为 [−231,  231 − 1]。请根据这个假设，如果反转后整数溢出那么就返回 0。
"""


class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        l = list(str(x))        # 注意[str(x)]：[chen, ..]     和    list(str(x))是个list函数：[c, h, e, n]，
        l = l[::-1]
        if l[-1] == '-':
            l.pop(-1)
            result = int('-'+''.join(l))
            if result < -2**31:
                return 0
            return result
        result = int(''.join(l))
        if result > 2**31:
            return 0
        return result
