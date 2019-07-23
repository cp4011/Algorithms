# 排列
def permutations(nums, k):
    res = []

    def dfs(nums, path):
        if len(path) == k:
            res.append(path)
        for i in range(len(nums)):
            dfs(nums[:i]+nums[i+1:], path+[nums[i]])        # 区别：组合只有nums[i+1:]
    dfs(nums, [])
    return res                                              # 如需去重，内部元素sort后，列表转成tuple()后set去重


# 组合
def combinations(nums, k):
    res = []

    def dfs(nums, path):
        if len(path) == k:                                  # 区别：子集中没有该判断
            res.append(path)
        for i in range(len(nums)):
            dfs(nums[i+1:], path+[nums[i]])
    dfs(nums, [])
    return res


# 子集
def subset(nums):
    res = []

    def dfs(nums, path):
        res.append(path)                # 每一步都在添加path
        for i in range(len(nums)):
            dfs(nums[i+1:], path+[nums[i]])
    dfs(nums, [])
    return res


print(permutations([1,2,3], 3))
print(combinations([1,2,3,4], 2))
print(subset([1,2,3]))
