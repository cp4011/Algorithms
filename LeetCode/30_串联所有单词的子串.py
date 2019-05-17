"""给定一个字符串 s 和一些长度相同的单词 words。找出 s 中恰好可以由 words 中所有单词串联形成的子串的起始位置。
注意子串要与 words 中的单词完全匹配，中间不能有其他字符，但不需要考虑 words 中单词串联的顺序。

示例 1：
输入：
  s = "barfoothefoobarman",
  words = ["foo","bar"]
输出：[0,9]
解释：
从索引 0 和 9 开始的子串分别是 "barfoor" 和 "foobar" 。
输出的顺序不重要, [9,0] 也是有效答案。

示例 2：
输入：
  s = "wordgoodgoodgoodbestword",
  words = ["word","good","best","word"]
输出：[]
"""


class Solution:
    def findSubstring(self, s, words):
        """因为单词长度固定的，可以计算出截取字符串的单词个数是否和 words 里相等，所以可以借用哈希表。一个是哈希表是 words，
一个哈希表是截取的字符串，比较两个哈希是否相等！因为遍历和比较都是线性的,所以时间复杂度：O(n^2)"""
        from collections import Counter
        if not s or not words:return []
        one_word = len(words[0])
        all_len = len(words) * one_word
        n = len(s)
        words = Counter(words)                    # Counter({'foo': 1, 'bar': 1}) 因为不在乎顺序，可只用字典记数
        res = []
        for i in range(0, n - all_len + 1):       # 计算数字 1_2_3 之间的空隔数量时：end - start，但是如果计算数字的个数end- start+1
            tmp = s[i:i+all_len]                  # 截取字符串s的长度
            c_tmp = []
            for j in range(0, all_len, one_word):   # 以每个单词的长度为等差来截取
                c_tmp.append(tmp[j:j+one_word])
            if Counter(c_tmp) == words:             # 若c_tmp也是 Counter({'foo': 1, 'bar': 1})，则将索引加入res中
                res.append(i)
        return res

    # 优化（滑动窗口）:一直在 s 维护着所有单词长度总和的一个长度队列。时间复杂度：O(n) n是s的长度【第一个for：O(每个单词的长度m),第二个O(n/m)】
    def findSubstring1(self, s, words):
        from collections import Counter
        if not s or not words:return []
        one_word = len(words[0])
        word_num = len(words)
        n = len(s)
        if n < one_word:return []
        words = Counter(words)
        res = []
        for i in range(0, one_word):
            cur_cnt = 0
            left = i
            right = i
            cur_Counter = Counter()
            while right + one_word <= n:
                w = s[right:right + one_word]
                right += one_word
                if w not in words:
                    left = right
                    cur_Counter.clear()
                    cur_cnt = 0
                else:
                    cur_Counter[w] += 1
                    cur_cnt += 1
                    while cur_Counter[w] > words[w]:
                        left_w = s[left:left+one_word]
                        left += one_word
                        cur_Counter[left_w] -= 1
                        cur_cnt -= 1
                    if cur_cnt == word_num:
                        res.append(left)
        return res
