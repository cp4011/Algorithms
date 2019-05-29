"""给定一个字符串 s1，我们可以把它递归地分割成两个非空子字符串，从而将其表示为二叉树。
下图是字符串 s1 = "great" 的一种可能的表示形式。
    great
   /    \
  gr    eat
 / \    /  \
g   r  e   at
           / \
          a   t
在扰乱这个字符串的过程中，我们可以挑选任何一个非叶节点，然后交换它的两个子节点。
例如，如果我们挑选非叶节点 "gr" ，交换它的两个子节点，将会产生扰乱字符串 "rgeat" 。
    rgeat
   /    \
  rg    eat
 / \    /  \
r   g  e   at
           / \
          a   t
我们将 "rgeat” 称作 "great" 的一个扰乱字符串。
同样地，如果我们继续将其节点 "eat" 和 "at" 进行交换，将会产生另一个新的扰乱字符串 "rgtae" 。
    rgtae
   /    \
  rg    tae
 / \    /  \
r   g  ta  e
       / \
      t   a
我们将 "rgtae” 称作 "great" 的一个扰乱字符串。
给出两个长度相等的字符串 s1 和 s2，判断 s2 是否是 s1 的扰乱字符串。
示例 1:
输入: s1 = "great", s2 = "rgeat"
输出: true
示例 2:
输入: s1 = "abcde", s2 = "caebd"
输出: false
"""


class Solution:
    def isScramble(self, s1, s2):
        n, m = len(s1), len(s2)
        if n != m or sorted(s1) != sorted(s2):
            return False
        if n < 4 or s1 == s2:
            return True
        f = self.isScramble
        for i in range(1, n):
            if f(s1[:i], s2[:i]) and f(s1[i:], s2[i:]) or f(s1[:i], s2[-i:]) and f(s1[i:], s2[:-i]):
                return True
        return False

    # 记忆化搜索（防止重复搜索）
    class Solution(object):
        """如果s1 前k个 跟s2后k个，是扰乱字符串，那么只要看s1第k+1个到最后 与 s2第0个到len(s2)-k个是否是扰乱字符串
如果s1 前k个 跟s2前k个，是扰乱字符串， 那么只要看s1， s2的第k+1个到最后是否是扰乱字符串,注意长度小于等于3的情形可以单独处理，简化代码"""
        def isScramble(self, s1, s2):
            memo = dict()

            def dfs(s1, s2):
                if (s1, s2) in memo: return memo[(s1, s2)]
                l1, l2 = len(s1), len(s2)
                if l1 != l2:
                    memo[(s1, s2)] = False
                    return False
                if l1 < 4:
                    memo[(s1, s2)] = sorted(s1) == sorted(s2)
                    return memo[(s1, s2)]
                if s1 == s2:  # 小范围单独处理的思想很重要
                    memo[(s1, s2)] = True
                    return True
                if sorted(s1) != sorted(s2):
                    return False
                memo[(s1, s2)] = False
                for k in range(1, l1):
                    a = s1[:k]
                    b = s2[:k]
                    c = s1[k:]
                    d = s2[k:]
                    e = s2[l1 - k:]
                    f = s2[:l1 - k]
                    if (dfs(a, b) and dfs(c, d)) or (dfs(a, e) and dfs(c, f)):
                        memo[(s1, s2)] = True
                        return memo[(s1, s2)]
                return memo[(s1, s2)]

            return dfs(s1, s2)
