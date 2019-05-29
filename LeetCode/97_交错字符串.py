"""给定三个字符串 s1, s2, s3, 验证 s3 是否是由 s1 和 s2 交错组成的。
示例 1:
输入: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
输出: true
示例 2:
输入: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
输出: false
"""


class Solution:
    # O(m*n) space
    def isInterleave1(self, s1, s2, s3):
        r, c, l = len(s1), len(s2), len(s3)
        if r + c != l:          # 长度不等，返回False
            return False
        dp = [[True for _ in range(c + 1)] for _ in range(r + 1)]   # 矩阵：字符串s2作为行（c+1列），字符串s1作为列（r+1行）
        for i in range(1, r + 1):                   # 初始化 第一列的各行的边界值
            dp[i][0] = dp[i - 1][0] and s1[i - 1] == s3[i - 1]
        for j in range(1, c + 1):                   # 初始化 第一行的各列的边界值
            dp[0][j] = dp[0][j - 1] and s2[j - 1] == s3[j - 1]
        for i in range(1, r + 1):           # 从1开始遍历
            for j in range(1, c + 1):
                dp[i][j] = (dp[i - 1][j] and s1[i - 1] == s3[i - 1 + j]) or (dp[i][j - 1] and s2[j - 1] == s3[i - 1 + j])
        return dp[-1][-1]

    # O(2*n) space
    def isInterleave2(self, s1, s2, s3):
        l1, l2, l3 = len(s1) + 1, len(s2) + 1, len(s3) + 1
        if l1 + l2 != l3 + 1:
            return False
        pre = [True for _ in range(l2)]
        for j in range(1, l2):
            pre[j] = pre[j - 1] and s2[j - 1] == s3[j - 1]
        for i in range(1, l1):
            cur = [pre[0] and s1[i - 1] == s3[i - 1]] * l2
            for j in range(1, l2):
                cur[j] = (cur[j - 1] and s2[j - 1] == s3[i + j - 1]) or \
                         (pre[j] and s1[i - 1] == s3[i + j - 1])
            pre = cur[:]
        return pre[-1]

    # O(n) space
    def isInterleave3(self, s1, s2, s3):
        r, c, l = len(s1), len(s2), len(s3)
        if r + c != l:
            return False
        dp = [True for _ in range(c + 1)]
        for j in range(1, c + 1):
            dp[j] = dp[j - 1] and s2[j - 1] == s3[j - 1]
        for i in range(1, r + 1):
            dp[0] = (dp[0] and s1[i - 1] == s3[i - 1])
            for j in range(1, c + 1):
                dp[j] = (dp[j] and s1[i - 1] == s3[i - 1 + j]) or (dp[j - 1] and s2[j - 1] == s3[i - 1 + j])
        return dp[-1]

    # DFS
    def isInterleave4(self, s1, s2, s3):
        r, c, l = len(s1), len(s2), len(s3)
        if r + c != l:
            return False
        stack, visited = [(0, 0)], set((0, 0))
        while stack:
            x, y = stack.pop()
            if x + y == l:
                return True
            if x + 1 <= r and s1[x] == s3[x + y] and (x + 1, y) not in visited:
                stack.append((x + 1, y))
                visited.add((x + 1, y))
            if y + 1 <= c and s2[y] == s3[x + y] and (x, y + 1) not in visited:
                stack.append((x, y + 1))
                visited.add((x, y + 1))
        return False

    # BFS
    def isInterleave(self, s1, s2, s3):
        r, c, l = len(s1), len(s2), len(s3)
        if r + c != l:
            return False
        queue, visited = [(0, 0)], set((0, 0))
        while queue:
            x, y = queue.pop(0)
            if x + y == l:
                return True
            if x + 1 <= r and s1[x] == s3[x + y] and (x + 1, y) not in visited:
                queue.append((x + 1, y))
                visited.add((x + 1, y))
            if y + 1 <= c and s2[y] == s3[x + y] and (x, y + 1) not in visited:
                queue.append((x, y + 1))
                visited.add((x, y + 1))
        return False
