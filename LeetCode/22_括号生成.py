"""给出 n 代表生成括号的对数，请你写出一个函数，使其能够生成所有可能的并且有效的括号组合。
例如，给出 n = 3，生成结果为：
[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
"""

# 回溯法:时间和空间复杂度都为：O(4^n / n^0.5)
'''只有在我们知道序列仍然保持有效时才添加 '(' or ')'，而不是像 暴力法 那样每次添加。我们可以通过跟踪到目前为止放置的左括号
和右括号的数目来做到这一点，如果我们还剩一个位置，我们可以开始放一个左括号。 如果它不超过左括号的数量，我们可以放一个右括号。'''


class Solution(object):
    def generateParenthesis(self, N):
        ans = []

        def backtrack(S='', left=0, right=0):
            if len(S) == 2 * N:                     # 有效序列长度达到 2N 的时候，即可添加入全局变量ans中
                ans.append(S)
                return
            if left < N:                            # 如果左括号( 还有剩余，我们可以放一个左括号
                backtrack(S+'(', left+1, right)
            if right < left:                        # 如果它不超过左括号的数量，我们可以放一个右括号
                backtrack(S+')', left, right+1)

        backtrack()
        return ans


# 暴力法：生成所有 2^2n个 '(' 和 ')' 字符构成的序列，然后检查每一个是否有效  时间和空间复杂度都为：O(2^2n * n)
"""为了生成所有序列，我们使用递归。长度为 n 的序列就是 '(' 加上所有长度为 n-1 的序列，以及 ')' 加上所有长度为 n-1 的序列。
为了检查序列是否为有效的，我们会跟踪 平衡，也就是左括号的数量减去右括号的数量的净值。如果这个值始终小于零或者不以零结束，
该序列就是无效的，否则它是有效的。"""


class Solution1(object):
    def generateParenthesis(self, n):
        def generate(A = []):
            if len(A) == 2*n:                   # 生成完一组2n个括号后，检查该组是否合法
                if valid(A):
                    ans.append("".join(A))      # 合法，则添加进 全局变量结果ans 中
            else:
                A.append('(')                   # 使用递归，生成所有序列
                generate(A)                     # 长度为 n 的序列就是 '(' 加上所有长度为 n-1 的序列，以及 ')' 加上所有长度为 n-1 的序列
                A.pop()
                A.append(')')
                generate(A)
                A.pop()

        def valid(A):                           # 检查括号序列是否合法
            bal = 0
            for c in A:
                if c == '(': bal += 1
                else: bal -= 1
                if bal < 0: return False        # 遍历的过程中 只要出现bal<0, 则直接返回False
            return bal == 0                     # 最后判断括号是否匹配成功

        ans = []
        generate()
        return ans
