'''给定一个非负整数，你至多可以交换一次数字中的任意两位。返回你能得到的最大值。
示例 1 :
输入: 2736
输出: 7236
解释: 交换数字2和数字7。

示例 2 :
输入: 9973
输出: 9973
解释: 不需要交换。
注意:     给定数字的范围是 [0, 108]
'''


def solve(nums):    # 给定一个非负整数，你至多可以交换一次数字中的任意两位。返回你能得到的最大值
    nums = list(str(nums))
    n = len(nums)
    dp = [n-1] * n
    temp = int(nums[-1])
    for i in range(n-2, -1, -1):        # 从右到左反向遍历，存下遍历到目前为止的最大数字的索引
        if int(nums[i]) > temp:
            temp = int(nums[i])
            dp[i] = i
        else:                           # 注意else条件
            dp[i] = dp[i+1]
    for i in range(n):
        if nums[dp[i]] != nums[i]:
            nums[dp[i]], nums[i] = nums[i], nums[dp[i]]     # 字符串str虽然可以取索引，但不能修改字符串的值，要转成list
            return int(''.join(nums))           # 至多可以交换一次数字中的任意两位
    return int(''.join(nums))


print(solve(2736))      # 7236


# 字节面试（思路对，实现出错）
def solve_interview(nums):
    nums = str(nums)
    n = len(nums)
    dp = [n-1] * n
    temp = int(nums[-1])
    for i in range(n-2, -1, -1):
        if int(nums[i]) > temp:
            temp = int(nums[i])
            dp[i] = i
        else:
            dp[i] = dp[i+1]
    for i in range(n):
        if nums[dp[i]] != nums[i]:
            nums[dp[i]], nums[i] = nums[i], nums[dp[i]]       # 字符串str虽然可以取索引，但不能修改字符串的值
    return nums

