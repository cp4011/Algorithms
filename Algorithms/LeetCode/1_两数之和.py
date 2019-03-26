"""给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。
你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。
示例:
给定 nums = [2, 7, 11, 15], target = 9
因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]
"""


# 查找记得要用 字典dict
def twoSum(nums, target):
    if len(nums) <= 1:
        return False
    dict = {}
    for i in range(len(nums)):
        j = target - nums[i]        # 查找 j
        if j in dict:
            return dict[j], i
        else:
            dict[nums[i]] = i       # 注意key是nums[i]，不是j


print(twoSum([3, 2, 4], 6))
# 错误代码
# def twoSum(nums, target):
#     for i in range(len(nums)):
#         j = target - nums[i]
#         if j in nums:
#             return i, nums.index(j)



