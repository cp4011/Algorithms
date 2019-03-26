"""给定一个序列，求解其中最长的递增子序列的长度"""


# 最长的递增子序列的长度：时间复杂度O(n*n)
def getdp1(arr):
    n = len(arr)
    dp = [0] * n
    for i in range(n):
        dp[i] = 1
        for j in range(i):
            if arr[i] > arr[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    return dp

# print(findNumberOfLIS([3, 1, 4, 5, 9, 2, 6, 5, 0]))   # 共4最长递增子序列个： 1 4 5 9; 1 4 5 6; 3 4 5 9; 3 4 5 6
# print(getdp1([3, 1, 4, 5, 9, 2, 6, 5, 0]))            # 最长递增子序列的长度是： 4


# 生成LIS序列
def generateLIS(arr, dp):
    n = max(dp)
    index = dp.index(n)
    lis = [0] * n
    n -= 1
    lis[n] = arr[index]
    for i in range(index, 0 - 1, -1):                           # 从右向左
        if arr[i] < arr[index] and dp[i] == dp[index] - 1:      # 关键
            n -= 1
            lis[n] = arr[i]
            index = i
    return lis


# 改进版：最长的递增子序列的长度：时间复杂度O(nlogn)：利用了二分查找 P206
def getdp2(arr):
    n = len(arr)
    dp, ends = [0] * n, [0] * n
    ends[0], dp[0] = arr[0], 1
    right, l, r, m = 0, 0, 0, 0
    for i in range(1, n):
        l = 0
        r = right
        # 二分查找,若找不到则ends[l或r]是比arr[i]大而又最接近其的数
        # 若arr[i]比ends有效区的值都大，则l=right+1
        while l <= r:
            m = (l + r) / 2
            if arr[i] > ends[m]:
                l = m + 1
            else:
                r = m - 1
        right = max(right, l)
        ends[l] = arr[i]
        dp[i] = l + 1
    return dp


'''
【最长*连续*递增子序列】
    dp[i]以nums[i]结尾的最长递增子序列的长度 if nums[i] > nums[j], 说明nums[i]能缀到nums[j]后面，那么dp[j]就能+1了
        dp[i+1] = max(dp[i + 1], dp[j] + 1)
'''


def findLengthOfLCIS(nums):
    if len(nums) == 0:
        return 0
    dp = [0 for _ in range(len(nums))]
    for i in range(len(nums)):
        dp[i] = 1                   # 如果不满足下面if的条件，即该数i大于前一个数，则dp数组该位置被置为1【连续递增断了，又要重新开始】
        if nums[i - 1] < nums[i]:
            dp[i] = dp[i - 1] + 1
    return max(dp)


"""LeetCode 673
给定一个未排序的整数数组，找到最长递增子序列的个数。
示例 1:
输入: [1,3,5,4,7]
输出: 2
解释: 有两个最长递增子序列，分别是 [1, 3, 4, 7] 和[1, 3, 5, 7]。
示例 2:
输入: [2,2,2,2,2]
输出: 5
解释: 最长递增子序列的长度是1，并且存在5个子序列的长度为1，因此输出5。
注意: 给定的数组长度不超过 2000 并且结果一定是32位有符号整数。
"""


# 最长递增子序列的个数
def findNumberOfLIS(nums):
    if not nums:
        return 0
    dp = [1] * len(nums)
    dp_2 = [1] * len(nums)
    for i in range(1, len(nums)):
        for j in range(i):
            if nums[i] > nums[j]:
                if dp[i] < dp[j] + 1:
                    dp[i] = dp[j] + 1
                    dp_2[i] = dp_2[j]
                elif dp[i] == dp[j] + 1:
                    dp_2[i] += dp_2[j]
    max_res = max(dp)
    ans = 0
    for i, num in enumerate(dp):
        if num == max_res:
            ans += dp_2[i]
    return ans