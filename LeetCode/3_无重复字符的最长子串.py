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


# 字典
def lengthOfLongestSubstring1(s):
    dic, res, start, = {}, 0, 0
    for i, ch in enumerate(s):
        if ch in dic:
            res = max(res, i-start)             # update the res
            start = max(start, dic[ch]+1)       # here should be careful, like "abba"
        dic[ch] = i
    return max(res, len(s)-start)               # return should consider the last non-repeated substring


# print(lengthOfLongestSubstring1("abcabcbb"))


"""
>>>seasons = ['Spring', 'Summer', 'Fall', 'Winter']
>>>list(enumerate(seasons))
[(0, 'Spring'), (1, 'Summer'), (2, 'Fall'), (3, 'Winter')]
>>>list(enumerate(seasons, start=1))       # 小标从 1 开始
[(1, 'Spring'), (2, 'Summer'), (3, 'Fall'), (4, 'Winter')]
"""