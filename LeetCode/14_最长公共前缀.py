"""编写一个函数来查找字符串数组中的最长公共前缀。
如果不存在公共前缀，返回空字符串 ""。

示例 1:
输入: ["flower","flow","flight"]
输出: "fl"

示例 2:
输入: ["dog","racecar","car"]
输出: ""
解释: 输入不存在公共前缀。
说明: 所有输入只包含小写字母 a-z 。
"""


class Solution:
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        longest_prefix = ''
        for i in range(len(strs[0])):
            cmp_s = strs[0][i]
            for _str in strs:
                if i == len(_str) or cmp_s != _str[i]:
                    return longest_prefix
            longest_prefix += cmp_s
        return longest_prefix
