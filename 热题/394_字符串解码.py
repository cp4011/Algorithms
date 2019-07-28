"""给定一个经过编码的字符串，返回它解码后的字符串。
编码规则为: k[encoded_string]，表示其中方括号内部的 encoded_string 正好重复 k 次。注意 k 保证为正整数。
你可以认为输入字符串总是有效的；输入字符串中没有额外的空格，且输入的方括号总是符合格式要求的。
此外，你可以认为原始数据不包含数字，所有的数字只表示重复的次数 k ，例如不会出现像 3a 或 2[4] 的输入。
示例:  s = "3[a]2[bc]", 返回 "aaabcbc".   s = "3[a2[c]]", 返回 "accaccacc".  s = "2[abc]3[cd]ef", 返回 "abcabccdcdcdef".
"""


class Solution:
    def decodeString(self, s: str) -> str:      # 涉及到括号匹配的问题用栈
        stack = []
        res = ''
        for i, _s in enumerate(s):
            if _s != ']':  # 不是右括号就一直进栈
                stack.append(_s)
            else:
                string = ''  # 先收集要加倍的字符串
                while not stack[-1].isnumeric():
                    string = stack.pop()+string
                times = ''  # 再收集加倍倍数
                while stack and stack[-1].isnumeric():
                    times = stack.pop()+times
                if times:  # 如果有倍数则加倍
                    string = string[1:]*int(times)
                if stack:  # 还有没处理完的上级，把处理好的字符串入栈等待处理
                    stack.append(string)
                else:  # 前面的字符串处理完毕了，直接把字符串加入答案
                    res += string
        return res + ''.join(stack)  # 最后可能有没有右括号收尾的字符串
