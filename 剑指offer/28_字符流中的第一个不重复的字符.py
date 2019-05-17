"""请实现一个函数用来找出字符流中第一个只出现一次的字符。例如，当从字符流中只读出前两个字符"go"时，第一个只出现一次的字符
是"g"。当从该字符流中读出前六个字符“google"时，第一个只出现一次的字符是"l"。
输出描述:如果当前字符流没有存在出现一次的字符，返回#字符。
"""
''' 用例:"google"
    对应输出应该为:"ggg#ll"        在后台循环调用函数，每次return只输出一个字符char
'''


class Solution:
    def __init__(self):
        self.s = ''
        self.dict1 = {}

    def FirstAppearingOnce(self):           # 返回对应char
        for i in self.s:                    # 因为dict映射是不记录key的顺序的，按照s记录的顺序去for循环遍历
            if self.dict1[i] == 1:
                return i
            # return '#'                    # 错误        你的输出为: "ggg###"
        return '#'                          # for循环遍历完所有的字符char后没发现有只出现一次的字符，输出 '#'

    def Insert(self, char):
        self.s += char                      # s 可以用来记录 各字符的顺序
        self.dict1[char] = self.dict1.get(char, 0) + 1
