"""给定一个只包含数字的字符串，复原它并返回所有可能的 IP 地址格式。
示例:
输入: "25525511135"
输出: ["255.255.11.135", "255.255.111.35"]
"""


class Solution(object):
    def restoreIpAddresses(self, s):
        def dfs(results, result, s, level):     # 深度优先遍历
            if len(s) == 0 and level == 4:
                results.add(".".join(result))
                return None
            if level >= 4:              # 超出4段ip的话就跳过
                return None
            for i in range(1, 4):        # 每个ip地址最多三位数字
                if s[:i] != "" and 0 <= int(s[:i]) <= 255:      # 保证每段ip不为空 且在0-255
                    if len(s[:i]) >= 2 and s[0] == "0":
                        continue                                # 保证每段ip没有 01.011.010这样的
                    dfs(results, result + [s[:i]], s[i:], level + 1)
        results = set()
        dfs(results, [], s, 0)
        return list(results)

    def restoreIpAddresses1(self, s):
        ans = []
        self.helper(ans, s, 4, [])
        return ['.'.join(x) for x in ans]

    def helper(self, ans, s, k, temp):
        if len(s) > k * 3:
            return
        if k == 0:
            ans.append(temp[:])
        else:
            for i in range(min(3, len(s) - k + 1)):
                if i == 2 and int(s[:3]) > 255 or i > 0 and s[0] == '0':
                    continue
                self.helper(ans, s[i + 1:], k - 1, temp + [s[:i + 1]])
