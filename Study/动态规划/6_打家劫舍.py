"""LeetCode 198
你是一个专业的小偷，计划偷窃沿街的房屋。每间房内都藏有一定的现金，影响你偷窃的唯一制约因素就是相邻的房屋装有相互连通的
防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。
给定一个代表每个房屋存放金额的非负整数数组，计算你在不触动警报装置的情况下，能够偷窃到的最高金额。
示例 1:
输入: [1,2,3,1]
输出: 4
解释: 偷窃 1 号房屋 (金额 = 1) ，然后偷窃 3 号房屋 (金额 = 3)。
     偷窃到的最高金额 = 1 + 3 = 4 。
示例 2:
输入: [2,7,9,3,1]
输出: 12
解释: 偷窃 1 号房屋 (金额 = 2), 偷窃 3 号房屋 (金额 = 9)，接着偷窃 5 号房屋 (金额 = 1)。
     偷窃到的最高金额 = 2 + 9 + 1 = 12 。
"""

'''
f(0) = nums[0]
f(1) = max(num[0], num[1])
f(k) = max( f(k-2) + nums[k], f(k-1) )
'''


# O(n)空间
def rob1(nums):
    if not nums:
        return 0
    if len(nums) <= 2:
        return max(nums)
    res = [0] * len(nums)
    res[0], res[1] = nums[0], max(nums[0], nums[1])
    for i in range(2, len(nums)):                       # range(10): python3返回的是一个range对象【生成器】，数据没有完全实例化,不必开辟一块很大的内存空间
        res[i] = max(nums[i]+res[i-2], res[i-1])        # list(range(10)): 列表
    return res[-1]


# 常数级空间
def rob(nums):
    if not nums:
        return 0
    if len(nums) <= 2:
        return max(nums)
    a, b = nums[0], max(nums[0], nums[1])
    for i in range(2, len(nums)):
        tmp = b
        b = max(nums[i]+a, b)
        a = tmp
    return b
