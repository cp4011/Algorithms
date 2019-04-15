"""LeetCode 648
在英语中，我们有一个叫做 词根(root)的概念，它可以跟着其他一些词组成另一个较长的单词——我们称这个词为 继承词(successor)。
例如，词根an，跟随着单词 other(其他)，可以形成新的单词 another(另一个)。现在，给定一个由许多词根组成的词典和一个句子。
你需要将句子中的所有继承词用词根替换掉。如果继承词有许多可以形成它的词根，则用最短的词根替换它。
你需要输出替换之后的句子。
示例 1:
输入: dict(词典) = ["cat", "bat", "rat"]
sentence(句子) = "the cattle was rattled by the battery"
输出: "the cat was rat by the bat"
注:
输入只包含小写字母。
1 <= 字典单词数 <=1000
1 <=  句中词语数 <= 1000
1 <= 词根长度 <= 100
1 <= 句中词语长度 <= 1000
"""
import collections


def replaceWords(dict, sentence):
    """
    :type dict: List[str]
    :type sentence: str
    :rtype: str  使用dict时，如果引用的Key不存在，就会抛出KeyError。如果希望key不存在时，返回一个默认值，就可以用defaultdict
    """
    d = collections.defaultdict(set)    # 除了在Key不存在时返回默认值，defaultdict的其他行为跟dict是完全一样的。
    s = collections.defaultdict(int)
    sentence = sentence.split()
    for word in dict:
        # print(word[0])
        d[word[0]].add(word)                # 以每个词根的首字母为键key，把词根放到该键所对应的值中去，这里的值是一个集合set
        s[word[0]] = max(s[word[0]], len(word))     # 同时记录该首字母所对应的词根的最大长度
    for i, word in enumerate(sentence):             # 遍历每个单词。enumerate()函数：索引index放到第一个变量，把元素放到第二个变量
        for j in range(s[word[0]]):         # 先把每个单词拿出来，查找以该单词开头的词根是否能够和这个单词匹配，s字典记录了
            if word[:j+1] in d[word[0]]:    # 以某个字母开头的词根的最大长度，从第一位开始截取，一直截取到最大长度，
                sentence[i] = word[:j+1]    # 若发现这个子字符串确实是一个词根的话，则修改单词，并结束该轮循环
                break
    return ' '.join(sentence)


# test
# dict = ["cat", "bat", "rat"]
# sentence = "the cattle was rattled by the battery"
# print(replaceWords(dict, sentence))


# 暴力法
# def replaceWords(dict, sentence):
#     s = sentence.split(" ")
#     for item in dict:                 # 遍历每一个词根
#         for i in range(len(s)):       # 遍历句子中的每个单词
#             n = len(item)
#             if item == s[i][:n]:      # 判断第i个单词s[i]的前n位和该词根是否相等
#                 s[i] = item           # 词根相等的话，将该单词赋值为该词根
#     return " ".join(s)                # 打印

