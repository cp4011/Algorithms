"""LeetCode 290 单词模式匹配
给定一种 pattern(模式) 和一个字符串 str ，判断 str 是否遵循相同的模式。
这里的遵循指完全匹配，例如， pattern 里的每个字母和字符串 str 中的每个非空单词之间存在着双向连接的对应模式。
示例1:
输入: pattern = "abba", str = "dog cat cat dog"
输出: true
示例 2:
输入:pattern = "abba", str = "dog cat cat fish"
输出: false
"""


def wordPattern(wordPattern, input):
    word = input.split(' ')                             # 如果两个字符串的长度不一样，则肯定不匹配
    if len(word) != len(wordPattern):
        return False
    hash = {}                                           # 记录模式字符串和目标字符串的对应关系
    used = {}                                           # 记录目前已经使用的字符串都有哪些【也可以用list，使用过的单词append进list就行】
    for i in range(len(wordPattern)):
        if wordPattern[i] in hash:                      # 检查模式字符串中的字符是否已经记录过映射关系
            if hash[wordPattern[i]] != word[i]:         # 不是第一次出现，则检查映射关系是否一致
                return False
        else:
            if word[i] in used:                         # 检查这个单词是否已经使用过，若使用过则返回不成立【因为其对应的模式都还没存在映射关系，但是该单词已经使用过了】
                return False
            hash[wordPattern[i]] = word[i]              # 第一次出现，则加入到哈希表即可
            used[word[i]] = True                        # 在used中保存哪些单词已经使用过
    return True
