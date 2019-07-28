"""给定一个非空字符串 s 和一个包含非空单词列表的字典 wordDict，判定 s 是否可以被空格拆分为一个或多个在字典中出现的单词。
说明：     拆分时可以重复使用字典中的单词。    你可以假设字典中没有重复的单词。
示例 1：   输入: s = "leetcode", wordDict = ["leet", "code"]
输出: true
解释: 返回 true 因为 "leetcode" 可以被拆分成 "leet code"。
示例 2：   输入: s = "applepenapple", wordDict = ["apple", "pen"]
输出: true
解释: 返回 true 因为 "applepenapple" 可以被拆分成 "apple pen apple"。
     注意你可以重复使用字典中的单词。
示例 3：   输入: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
输出: false
"""
class Solution:
    def wordBreak(self, s, wordDict):       # 动态规划
        """dp[i]表示s到i位置s[:i] 是否可以由wordDict组成, 如果dp[i - j]是true 并且s[j:i]在wordDict里, 那么dp[i] = true;"""
        n = len(s)
        if not wordDict:
            return not s
        dp = [False] * (n + 1)
        dp[0] = True
        for i in range(1, n + 1):                       # i从1开始，s[:i]=s[:1] 即从字符串s的第一个字符开始遍历
            for j in range(i - 1, -1, -1):              # 自底向上
                if dp[j] and s[j:i] in wordDict:        # dp[j]代表s[:j]
                    dp[i] = True
                    break
        return dp[-1]
