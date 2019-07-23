"""给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。
示例 1:
输入: "abcabcbb"
输出: 3
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
示例 2:
输入: "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
示例 3:
输入: "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
     请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。
"""


# 字典
def lengthOfLongestSubstring1(s):
    dic, res, start, = {}, 0, 0             # 字典：字符作为 key，该字符所在的索引位置i 作为key
    for i, ch in enumerate(s):              # enumerate()
        if ch in dic:
            res = max(res, i-start)         # 更新res
            start = max(start, dic[ch]+1)   # 此处要注意dic[ch]+1有可能会小于start|的，如"abba"，当遍历到最后一个a的时候ab|ba
        dic[ch] = i                         # 遇到重复的字符，将会覆盖掉前出现的字符的索引i
    return max(res, len(s)-start)           # 返回时应该考虑 最后一段不重复的子串


# 当一个子串第一个出现重复的时候，从第二个开始再计算个数，可以使用字符串的切片操作
def lengthOfLongestSubstring(s):
    max_num = 0
    num = 0
    st = ""

    for i in s:
        if i not in st:
            st += i
            num += 1
        else:
            if num > max_num:
                max_num = num
            index = st.index(i)
            st = st[index + 1:] + i
            num = len(st)
    if num > max_num:               # 注意考虑最后不重复的子串
        max_num = num
    return max_num
print(lengthOfLongestSubstring("aabaab!bb"))




# print(lengthOfLongestSubstring1("abcabcbb"))


"""
>>>seasons = ['Spring', 'Summer', 'Fall', 'Winter']
>>>list(enumerate(seasons))
[(0, 'Spring'), (1, 'Summer'), (2, 'Fall'), (3, 'Winter')]
>>>list(enumerate(seasons, start=1))       # 小标从 1 开始
[(1, 'Spring'), (2, 'Summer'), (3, 'Fall'), (4, 'Winter')]
"""