"""给定一个字符串 S 和一个字符串 T，请在 S 中找出包含 T 所有字母的最小子串。
示例：
输入: S = "ADOBECODEBANC", T = "ABC"
输出: "BANC"
说明：
如果 S 中不存这样的子串，则返回空字符串 ""。
如果 S 中存在这样的子串，我们保证它是唯一的答案。
"""


# 优化版的【滑动窗口】:在更短的字符filtered_S中使用滑动窗口法（定义l、r两指针）。
# 建立filtered_S列表，其中包括 S中的全部字符以及它们在S的下标，但这些字符必须在 T 中出现。
# S = "ABCDDDDDDEEAFFBC" T = "ABC" filtered_S = [(0, 'A'), (1, 'B'), (2, 'C'), (11, 'A'), (14, 'B'), (15, 'C')]
def minWindow(s, t):
    """在 S 中找出包含 T 所有字母的最小子串:  1. 初始，left指针和right指针都指向S的第一个元素.    2.将 right指针右移，扩张窗
    口，直到得到一个    可行窗口，亦即包含T的全部字母的窗口。   3. 得到可行的窗口后，将left指针逐个右移，若得到的窗口依然可行，
    则更新最小窗口大小。  4. 若窗口不再可行，则跳转至 2"""
    if not t or not s: return ""
    from collections import Counter
    dict_t = Counter(t)             # 对 T ：字典记数
    required = len(dict_t)          # 字符串T中总共有几个不同的字符（每个字符可能有多个）
    filtered_s = []                 # 定义一个更短的字符串filtered_S列表，其中包括 S中全部字符且在T中出现的，以及它们在S的下标
    for i, char in enumerate(s):        # 枚举索引及字符
        if char in dict_t:              # 若该字符在T中出现，则加入到 更短的字符串filtered_S中
            filtered_s.append((i, char))
    l, r = 0, 0
    formed = 0                      # 当前窗口中满足T中某个字符出现次数的个数，与required相等时，则证明当前窗口是可行窗口
    window_counts = {}              # 定义两指针l、r所维护中间的当前窗口字典
    ans = float("inf"), None, None
    while r < len(filtered_s):      # 只需遍历 更短的过滤后s中只包含T中字符的字符串，不需要再次遍历整个字符串S了
        character = filtered_s[r][1]
        window_counts[character] = window_counts.get(character, 0) + 1
        if window_counts[character] == dict_t[character]:   # 当满足某个字符在字符串T中出现的次数，则formed +1
            formed += 1                         # formed：直到与required相等即表示形成可行窗口
        while l <= r and formed == required:    # 若当前窗口含有所有T中所有字母，且l <= r，左指针l右移，缩小窗口
            character = filtered_s[l][1]
            end = filtered_s[r][0]              # 记录目前最小的可行窗口
            start = filtered_s[l][0]
            if end - start + 1 < ans[0]:
                ans = (end - start + 1, start, end)
            window_counts[character] -= 1       # 左指针l右移一位以后，当前窗口中该字符的记数-1
            if window_counts[character] < dict_t[character]:   # 若当前窗口删除的该元素正是T中的一个字符，则此时不满足需要字符的个数了
                formed -= 1
            l += 1
        r += 1
    return "" if ans[0] == float("inf") else s[ans[1]: ans[2] + 1]
