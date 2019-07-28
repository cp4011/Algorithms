"""有 n 个气球，编号为0 到 n-1，每个气球上都标有一个数字，这些数字存在数组 nums 中。
现在要求你戳破所有的气球。每当你戳破一个气球 i 时，你可以获得 nums[left] * nums[i] * nums[right] 个硬币。 这里的
 left 和 right 代表和 i 相邻的两个气球的序号。注意当你戳破了气球 i 后，气球 left 和气球 right 就变成了相邻的气球。
求所能获得硬币的最大数量。
说明:     你可以假设 nums[-1] = nums[n] = 1，但注意它们不是真实存在的所以并不能被戳破。
0 ≤ n ≤ 500, 0 ≤ nums[i] ≤ 100
示例:     输入: [3,1,5,8]
输出: 167
解释: nums = [3,1,5,8] --> [3,5,8] -->   [3,8]   -->  [8]  --> []
     coins =  3*1*5      +  3*5*8    +  1*3*8      + 1*8*1   = 167
"""


class Solution:
    def maxCoins(self, nums):
        if not nums:
            return 0
        nums = [1] + nums + [1]  # 设置哨兵
        l = len(nums)
        dp = [[0] * l for _ in range(l)]  # dp[i][j]表示戳破 [i+1...j-1] 号气球的最大收益，保留i,j，因为哨兵的气球不能被戳破,

        for j in range(2, l):                   # j从2开始
            for i in range(j - 2, -1, -1):      # 从i到j
                for k in range(i + 1, j):       # 戳破k位置上的气球
                    dp[i][j] = max(dp[i][j], dp[i][k] + dp[k][j] + nums[i] * nums[k] * nums[j])
        return dp[0][-1]


print(Solution().maxCoins([3, 1, 5, 8]))
