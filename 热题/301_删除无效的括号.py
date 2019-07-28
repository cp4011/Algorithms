"""删除最小数量的无效括号，使得输入的字符串有效，返回所有可能的结果。
说明: 输入可能包含了除 ( 和 ) 以外的字符。
示例 1:
输入: "()())()"
输出: ["()()()", "(())()"]
示例 2:
输入: "(a)())()"
输出: ["(a)()()", "(a())()"]
示例 3:
输入: ")("
输出: [""]
"""
''' 算法：递归
    用l和r记录不匹配的左括号数量和右括号数量
    然后从0位置开始递归，如果l == 0 and r == 0 并且做移除不合法括号处理后的字符串是合法的话，即isValid的话，
    就添加到结果集中
    在递归的时候，先移除右括号，再移除左括号，因为先移除右括号后能保障前面的序列prefix是合法的序列，然后再从后面的
    字符串中移除左括号，如果先移除左括号，后面的右括号不匹配的数量就会变多（花花酱的视频里是这么说的，但是我调换了
    左右顺序后发现并不影响）。
    遍历的时候，重复出现的左括号或者右括号，只删除最开头的那个就好了，所if s[i] == s[i-1]:continue，但是要求
     i-1 >= start
    如果s[i]是')'，如果r > 0说明有右括号不匹配，移除第i个位置的字符，向下递归，新的字符串就是s[:i] + s[i + 1:]，
    同时 r - 1
    如果s[i]是'('，如果l > 0说明有左括号不匹配，移除第i个位置的字符，向下递归，新的字符串就是s[:i] + s[i + 1:]
    同时 l - 1
    向下传的start = i，也就是说下面的处理就只处理第i位置开始的了，事实上由于当前会删一个字符，所以后面的字符会向前
    挪一个，一般来说应该是range(start+1,len(s))，但是由于第i个位置的字符删掉了，后面的字符向前挪了一位，所以向下
    的时候从start = i的位置处理其实就相当于原来的处理第start+1也就是i+1的位置的字符，所以是合理的，向后逐位处理
    所以整体的策略就是先检测出字符串中需要删除的左右括号的数量，然后逐个删除，直到l = r = 0，然后如果此时的s是合法的话
    就可以添加进结果中了。删除的时候从前向后，先删右括号再删左括号'''


class Solution:
    def removeInvalidParentheses(self, s):
        def isValid(s):                 # 验证目前的s中左右括号数目是否匹配
            count = 0
            for char in s:
                if char == '(':
                    count += 1
                if char == ')':
                    count -= 1
                if count < 0:
                    return False  # ())))
            return count == 0

        def dfs(s, start, l, r):
            if l == 0 and r == 0:       # 如果左右括号匹配，添加进结果集
                if isValid(s):
                    self.ans.append(s)
                return
            for i in range(start, len(s)):      # 如果左右不匹配
                if i - 1 >= start and s[i] == s[i - 1]:     # 如果i和前一个相同，那么删哪个结果都一样，故跳过
                    continue
                if r > 0 and s[i] == ')':                   # 如果右括号有不匹配的，删去右括号，判断是否匹配
                    dfs(s[:i] + s[i + 1:], i, l, r - 1)
                if l > 0 and s[i] == '(':                   # 如果左括号有不匹配的，删去左括号，判断是否匹配
                    dfs(s[:i] + s[i + 1:], i, l - 1, r)
        l = 0
        r = 0
        for char in s:      # 统计右括号不匹配的数量放入r，左括号没有被匹配的数量放入l
            if char == '(':
                l += 1
            elif char == ')':
                if l == 0:
                    r += 1
                else:
                    l -= 1
        self.ans = []
        dfs(s, 0, l, r)
        return self.ans
