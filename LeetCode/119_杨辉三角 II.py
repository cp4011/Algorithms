"""给定一个非负索引 k，其中 k ≤ 33，返回杨辉三角的第 k 行。
在杨辉三角中，每个数是它左上方和右上方的数的和。
示例:
输入: 3
输出: [1,3,3,1]
进阶： 你可以优化你的算法到 O(k) 空间复杂度吗？
"""


def getRow(rowIndex):
    tmp = []    # []    [1]   [1,1]    [1,2,1]     [1,3,3,1]
    for _ in range(rowIndex + 1):   # 循环4次
        tmp.insert(0, 1)    # 每次循环，数组都头部插入1，[1]   [1,1]   [1,1,1]    [1,1,2,1]
        for i in range(1, len(tmp) - 1):
            tmp[i] = tmp[i] + tmp[i+1]      # [1,2,1]   [1,3,3,1]
    return tmp


print(getRow(3))
