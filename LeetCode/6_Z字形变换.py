"""将一个给定字符串根据给定的行数，以从上往下、从左到右进行 Z 字形排列。
比如输入字符串为 "LEETCODEISHIRING" 行数为 3 时，排列如下：
L   C   I   R
E T O E S I I G
E   D   H   N
之后，你的输出需要从左往右逐行读取，产生出一个新的字符串，比如："LCIRETOESIIGEDHN"。
请你实现这个将字符串进行指定行数变换的函数：
string convert(string s, int numRows);
示例 1:
输入: s = "LEETCODEISHIRING", numRows = 3
输出: "LCIRETOESIIGEDHN"
示例 2:
输入: s = "LEETCODEISHIRING", numRows = 4
输出: "LDREOEIIECIHNTSG"
解释:
L     D     R
E   O E   I I
E C   I H   N
T     S     G
"""

'''找规律
Z字形，就是两种状态，一种垂直向下，还有一种斜向上
0               2n-2
1           .
.       .
.   n
n-1
每一个Z字的首字母差，2n-2 位置
除去首尾两行，每个 Z 字有两个字母，索引号关系为，一个为 i，另一个为 numsRows*2-2-i'''


# 每个索引被访问一次，时间复杂度：O(n)
class Solution:
    def convert(self, s, numRows):
        if not s:
            return ""
        if numRows == 1:
            return s
        length = len(s)
        split_length = 2 * numRows - 2
        data = []
        res = ''
        for i in range(0, length, split_length):        # 将字符串s分成众多子串，子串长度为2* numRows-2【子串的循环周期】
            data.append(s[i:i+split_length])            # 将切分后的各子串作为元素，放入列表中，以便后续遍历
        for i in range(numRows):            # 遍历已经形成 Z字形字符串 的每一行【索引】
            for sub_s in data:              # 遍历子串
                if i < len(sub_s):          # 判断最后一个s切分下来的子串有可能没有numsRows这么多个元素，会造成数字下标越界
                    if i == 0 or i == numRows - 1:      # 判断i是否在收尾两行，如果是，则只用加上一位子串里的元素
                        res += sub_s[i]
                    else:                               # 不是收尾两行的元素，则需要加上两位子串中的元素
                        res += sub_s[i]
                        if split_length - i < len(sub_s):   # 添加第二位元素时，还需要判断该元素的索引是否越界【有可能最后一个子串元素不够，造成数组下标越界】
                            res += sub_s[2*numRows-2 - i]
        return res
