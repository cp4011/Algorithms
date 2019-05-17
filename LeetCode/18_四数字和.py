"""给定一个包含 n 个整数的数组 nums 和一个目标值 target，判断 nums 中是否存在四个元素 a，b，c 和 d ，使得 a + b + c + d
的值与 target 相等？找出所有满足条件且不重复的四元组。
注意：
答案中不可以包含重复的四元组。

示例：
给定数组 nums = [1, 0, -1, 0, -2, 2]，和 target = 0。
满足要求的四元组集合为：
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]
"""


class Solution:
    def fourSum(self, nums, target):
        import collections, itertools
        two_sum = collections.defaultdict(list)     # list 返回[], int 返回的是 0
        res = set()                                 # 集合添加元素 set.add()
        for (n1, i1), (n2, i2) in itertools.combinations(enumerate(nums), 2):
            two_sum[i1+i2].append({n1, n2})         # 列表[]中append：集合【该键值a+b，可能有多个集合的下标】如：{0：[{0,2},{1,3},{4,5}],....}
        for t in list(two_sum.keys()):              # Python3 字典 keys()方法返回一个可迭代对象，可以使用 list() 来转换为列表。
            if not two_sum[target-t]:               # 没有默认返回的是 []
                continue
            for pair1 in two_sum[t]:                # 已经确认该键t(a+b)下，有另外一对键target-t满足题意的情况下，遍历该键t的值列表
                for pair2 in two_sum[target-t]:     # 如t=0，则two_sum[t]为列表 [{0,2},{1,3},{4,5}]，依次遍历
                    if pair1.isdisjoint(pair2):     # set.isdisjoint(set) 判断两个集合是否包含相同的元素，如果没有返回 True，否则返回 False
                        res.add(tuple(sorted([nums[i] for i in pair1 | pair2])))   # 并集。sorted返回的是列表不能被集合hash，要转成元组tuple。两集合 x&y交集 x|y并集 x-y差集
            del two_sum[t]                      # 删除字典中已经遍历的项
        return [list(r) for r in res]           # return a list of lists of length 4, [[val1,val2,val3,val4]]


# print(list(enumerate([-2, -1, 0, 0, 1, 2])))        # [(0, -2), (1, -1), (2, 0), (3, 0), (4, 1), (5, 2)]
# disjoint 互斥的，不相交的


