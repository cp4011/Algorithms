"""LeetCode 1
给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。
你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。
示例:
给定 nums = [2, 7, 11, 15], target = 9
因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]"""
"""字典dict实现哈希法，key映射value"""


# 哈希法（字典）
def twoSum(nums, target):
    dict = {}                                         # 字典实现哈希法，key映射value
    for i in range(len(nums)):
        m = nums[i]
        if target - m in dict:                        # 判定target-m是否已经在字典之中
            return dict[target - m] + 1, i + 1        # 如果已经存在，则返回这两个数的下标【注意下标+1】
        dict[m] = i                                   # 如果不存在 则记录键值对
# test
# nums = [int(i) for i in input().strip().split()]
# target = int(input())
# print(twoSum(nums, target))


# 双指针法（算法复杂度高）
def twoSum2(nums, target):
    res= []   				# 存放结果编号数据
    newnums= nums[:]		# 深拷贝，把原数据拷贝到newnums里
    newnums.sort()			# 对新数组排序
    left = 0
    right = len(newnums) - 1                            # 定义left和right指针分别指向新数组的开头和结尾
    while left < right:
        if newnums[left] + newnums[right] == target:
            for i in range(0, len(nums)):	            # 在原始数组中寻找第一个元素的原始下标
                if nums[i] == newnums[left]:
                    res.append(i)			            # 下标加入到结果集
                    break
                for i in range(len(nums)-1, -1, -1):    # 在原始数组中寻找第二个元素的原始下标
                    if nums[i] == newnums[right]:
                        res.append(i)			        # 下标加入到结果集
                        break
            res.sort()
            break
        elif newnums[left] + newnums[right] < target:
            left = left + 1				                # 让left指针向右移动一位
        elif newnums[left] + newnums[right] > target:
            right = right - 1			                # 让right指针向左移动一位
    return res[0]+1, res[1]+1	                        # 返回结果集



