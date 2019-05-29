"""公园里有N个花园，初始时每个花园里都没有种花，园丁将花园从1到N编号并计划在编号为i的花园里恰好种A_i朵花，他每天会选择一个
区间[L，R]（1≤L≤R≤N）并在编号为L到R的花园里各种一朵花，那么园丁至少要花多少天才能完成计划？
输入描述:
第一行包含一个整数N，1≤N≤10^5。    第二行包含N个空格隔开的整数A_1到A_N，0≤A_i≤10^4。
输出描述:   输出完成计划所需的最少天数。
输入例子1:
5
4 1 8 2 5
输出例子1:
14
"""
'''从最大的开始，假设最大的值序号为idx，与idx-1和idx+1的中的较大值比较，count加上idx与较大值的差，然后删掉idx，循环。'''


def solve(n, nums):
    """    单调栈：栈内只存储递增元素    时间复杂度O(n)    """
    nums.append(0)              # 输入nums: 4 1 8 2 5   添加一个0
    stack = []
    res = 0
    for i in range(n + 1):
        if not stack or stack[-1] <= nums[i]:
            stack.append(nums[i])
        else:
            res += stack[-1] - nums[i]          # +3  +6  +5
            while stack and stack[-1] > nums[i]:
                stack.pop()
            stack.append(nums[i])               # 最后剩 [1, 2, 0]
    print(res)


n = int(input())
nums = [int(x) for x in input().split()]
solve(n, nums)
