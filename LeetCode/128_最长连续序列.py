"""给定一个未排序的整数数组，找出最长连续序列的长度。要求算法的时间复杂度为 O(n)。
示例: 输入: [100, 4, 200, 1, 3, 2]
输出: 4
解释: 最长连续序列是 [1, 2, 3, 4]。它的长度为 4。
"""
def longestConsecutive(nums):
    if not nums:                    # 注意输入是空数组的情况 []
        return 0
    dict = {}                       # 查找 用 字典
    for num in nums:
        dict[num] = 1
    longest = 1
    for num in nums:
        count = 1
        pre = num - 1
        while pre in dict:          # num - 1 这数字是否在字典里
            del dict[pre]
            count += 1
            pre -= 1                # 继续 减， 往下找
        next = num + 1
        while next in dict:         # 往上找
            del dict[next]
            count += 1
            next += 1
        if longest < count:
            longest = count
    return longest


# 自己用数组实现的（成功，但效率不高）【用字典效率高】
def fun(nums):
    if not nums:
        return 0
    longest = 0
    for num in nums:
        count = 1
        pre = num - 1
        while pre in nums:
            nums.remove(pre)            # 数组删除指定元素 list.remove()
            while nums.count(pre) != 0:
                nums.remove(pre)
            count += 1
            pre -= 1

        next = num + 1
        while next in nums:
            nums.remove(next)
            while nums.count(next) != 0:
                nums.remove(next)
            count += 1
            next += 1

        if longest < count:
            longest = count
    return longest


print(fun([100, 4, 200, 1, 3, 2]))
