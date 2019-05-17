"""给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。
有效字符串需满足：

左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
注意空字符串可被认为是有效字符串。

示例 1:
输入: "()"
输出: true
示例 2:
输入: "()[]{}"
输出: true
示例 3:
输入: "(]"
输出: false
示例 4:
输入: "([)]"
输出: false
示例 5:
输入: "{[]}"
输出: true
"""

'''注意两个方面：
    1. 栈stack为空
    2. 栈stack 遍历完以后 还剩下元素
'''


class Solution:
    def isValid(self, s):
        mapping = {"}": "{", ")": "(", "]": "["}        # 左括号 到 右括号 的映射
        stack = []                                      # 定义栈

        for ch in s:                                    # 遍历字符串中的每一个字符
            if ch in ['[', '{', '(']:
                stack.append(ch)                        # 栈中压入 左括号
            else:
                if stack:                               # 注意判断当前栈stack 是否为空
                    if stack.pop() != mapping[ch]:
                        return False
                else:
                    return False
        if stack:                                       # 注意遍历完后，栈stack中还有括号没有处理
            return False
        else:
            return True
