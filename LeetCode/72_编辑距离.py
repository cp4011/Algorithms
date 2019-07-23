"""给定两个单词 word1 和 word2，计算出将 word1 转换成 word2 所使用的最少操作数 。
你可以对一个单词进行如下三种操作：   插入一个字符     删除一个字符      替换一个字符
示例 1:   输入: word1 = "horse", word2 = "ros"      输出: 3
解释:
horse -> rorse (将 'h' 替换为 'r')      rorse -> rose (删除 'r')      rose -> ros (删除 'e')
"""
'''通过两个指针i和j分别指向word1和word2。我们定义函数f(i,j) 表示word1[:i]转换为word2[:j]需要的最少步骤
首先要比较word1[i-1]和word2[j-1]是不是相同，如果相同的话就不用做任何操作，所以此时f(i,j)=f(i−1,j−1) （i和j都向前挪一个位置）。
对于不相同的时候:有三种处理手段，分别是insert、replace和remove。
    1. insert操作。insert完之后，也就是word1中的元素会保持不变，而j会向前挪一个位置，也就是f(i,j)=f(i,j−1)+1 。
    2. replace操作，replace会减少word1和word2中一个需要比较的元素（i和j会向前挪一个位置），也就是f(i,j)=f(i−1,j−1)+1。
    3. remove操作，这个就很容易了，word1中会减少一个需要比较的元素，而我们j的位置不变，也就是f(i,j)=f(i−1,j)+1 。最后结果三者取最小值
    初始条件:也就是word1和word2为空的情况，此时也非常简单f(i,0)=i 、f(0,j)=j'''


class Solution(object):
    def minDistance(self, word1, word2):        # O(m*n) space 矩阵：动态规划
        m, n = len(word1), len(word2)
        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        for i in range(m + 1): dp[i][0] = i     # word1变成0需要的每个层次的步数
        for j in range(n + 1): dp[0][j] = j     # 初始化边界
        for i in range(1, m + 1):
            for j in range(1, n + 1):           # word1的下标i-1，word2的下标为j-1（当j最大=n时，指针j指到word2最后一个字母word2[n-1]）
                dp[i][j] = min(dp[i - 1][j - 1] + (0 if word1[i - 1] == word2[j - 1] else 1), dp[i - 1][j] + 1, dp[i][j - 1] + 1)
        return dp[m][n]

    # O(n) space 数组：动态规划
    def minDistance1(self, word1, word2):
        l1, l2 = len(word1) + 1, len(word2) + 1
        pre = [0 for _ in range(l2)]
        for j in range(l2):
            pre[j] = j
        for i in range(1, l1):
            cur = [i] * l2
            for j in range(1, l2):
                cur[j] = min(cur[j - 1] + 1, pre[j] + 1, pre[j - 1] + (word1[i - 1] != word2[j - 1]))
            pre = cur[:]
        return pre[-1]
