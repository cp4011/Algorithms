"""报数序列是一个整数序列，按照其中的整数的顺序进行报数，得到下一个数。其前五项如下：
1.     1
2.     11
3.     21
4.     1211
5.     111221
1 被读作  "one 1"  ("一个一") , 即 11。
11 被读作 "two 1s" ("两个一"）, 即 21。
21 被读作 "one 2",  "one 1" （"一个二" ,  "一个一") , 即 1211。

给定一个正整数 n（1 ≤ n ≤ 30），输出报数序列的第 n 项。 注意：整数顺序将表示为一个字符串。

示例 1:
输入: 1
输出: "1"

示例 2:
输入: 4
输出: "1211"
"""

''' 不断由前一个数推下一个数. 
    对当前字符串进行遍历，记录下重复的数字及其数量; 将记录下在数据赋值给字符串，再重复执行'''


class Solution:
    def countAndSay(self, n: int) -> str:

        def next_num(s):
            res = ""                            # 记录本轮产生的 结果
            i = 0
            N = len(s)
            while i < N:
                count = 1
                while i < N - 1 and s[i] == s[i+1]:
                    count += 1                  # 记录重复的个数
                    i += 1
                res += (str(count) + s[i])      # 该数字的重复个数 以及 该数字
                i += 1
            return res

        res = "1"
        for i in range(1, n):                   # 从 1（第二个）开始，根据前一个res推出下一个res
            res = next_num(res)                 # 不断由 前一个res 推出 下一个res
        return res
