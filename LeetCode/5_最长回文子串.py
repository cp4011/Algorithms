"""给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。
示例 1：
输入: "babad"
输出: "bab"
注意: "aba" 也是一个有效答案。
示例 2：
输入: "cbbd"
输出: "bb"
"""


# 将s反转后，逐位进行对比
def longestPalindrome(s):
    if s == '':
        return s
    ss = s[::-1]
    s_len = len(s)
    res_len = 1
    res_str = s[0]
    for i in range(s_len):
        for j in range(i + res_len + 1, s_len + 1):
            if s[i:j] == ss[s_len - j:s_len - i]:
                res_len = j - i
                res_str = s[i:j]
    return res_str

print(longestPalindrome("babad"))


"""最长公共子串(反转 S，使之变成 S' 。找到 S 和 S' 之间最长的公共子串，这也必然是最长的回文子串。)
有缺陷：例如，S = “caba”, S' = “abac”S以及 S'之间的最长公共子串为 “aba”，恰恰是答案。
但是S=“abacdfgdcaba” , S ′ =“abacdgfdcaba”：S 以及 S′之间的最长公共子串为“abacd”，显然，这不是回文。
【当 S 的其他部分中存在非回文子串的反向副本时，最长公共子串法就会失败。为了纠正这一点，每当我们找到最长的公共子串的候选
项时，都需要检查子串的索引是否与反向子串的原始索引相同。如果相同，那么我们尝试更新目前为止找到的最长回文子串；如果不是，
我们就跳过这个候选项并继续寻找下一个候选。】
"""