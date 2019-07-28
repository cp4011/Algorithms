"""给你一个 n * m 的数字矩阵，现在要求你找到两个既不在同一行也不再同一列的数字，使得乘积最大"""
'''可简化，以其中的两行为例：
若第一行的最大值的序号与第二行的最大值的序号互异，则这两行乘积的最大值为两行分别的最大值相乘；
若第一行的最大值得序号与第二行的最大值的序号相等，说明某一行的最大值的序号与另一行的第二大值得序号必互异，则乘积最大值在
某一行的最大值与另一行的第二大的值的乘积当中（共有两个，取最大的）'''
nums = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
n = len(nums)
m = len(nums[0])
target = []
for i in range(n):
    tmp = [[-float("inf"), -1], [-float("inf"), -1]]  # 存储当前行的最大值，第二大的值以及他们各自的序号
    for j in range(m):
        if nums[i][j] > tmp[0][0]:      # 遇到更大值
            tmp[1] = tmp[0][:]          # 复制第二大的值和索引
            tmp[0][0] = nums[i][j]      # 记录最大值和索引
            tmp[0][1] = j
    target.append(tmp)

max_ = -float("inf")
for i in range(n):
    for j in range(i + 1, n):
        if target[i][0][1] != target[j][0][1]:  # 如果最大值两个列序号不相等，则这两行的最大值是两行各自最大值的乘积
            max_ = max(target[i][0][0] * target[j][0][0], max_)
        else:  # 反之则说明这两行中某一行的最大值的序号和另一行的第二大的值的序号是互异的
            max_ = max(target[i][0][0] * target[j][1][0], target[i][1][0] * target[j][0][0], max_)
print(max_)


# 矩阵成绩最大（不同行，不同列的两个数） 【60%】
def func(n, m, mat):
    dict1 = {}
    for i in range(n):
        for j in range(m):
            dict1[(i, j)] = mat[i][j]
    dict2 = sorted(dict1.items(), key=lambda x: x[1], reverse=True)
    res = -999999999
    for i in range(n*m):
        for j in range(i+1, n*m):
            if dict2[i][0][0] != dict2[j][0][0] and dict2[i][0][1] != dict2[j][0][1]:
                res = max(res, dict2[i][1] * dict2[j][1])
    return res


n, m = map(int, input().split())
mat = []
for i in range(n):
    mat.append([int(i) for i in input().split()])
print(func(n, m, mat))

