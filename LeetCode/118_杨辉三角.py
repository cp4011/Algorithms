"""给定一个非负整数 numRows，生成杨辉三角的前 numRows 行。
在杨辉三角中，每个数是它左上方和右上方的数的和。
示例:
输入: 5
输出:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
"""


class Solution:
    def generate(self, numRows):        # 在杨辉三角中，每个数是它左上方和右上方的数的和。
        res = []
        while numRows:
            tmp = [1]
            if not res:
                res.append(tmp)
            else:
                n = len(res[-1])
                for i in range(n - 1):
                    tmp.append(res[-1][i] + res[-1][i + 1])
                tmp.append(1)
                res.append(tmp)
            numRows -= 1
        return res

    def generate0(self, numRows):   # 简化版
        res = []
        tmp = []
        for _ in range(numRows):
            tmp.insert(0, 1)
            for i in range(1, len(tmp) - 1):
                tmp[i] = tmp[i] + tmp[i + 1]
            res.append(tmp[:])
        return res

    def generate1(self, num_rows):
        triangle = []
        for row_num in range(num_rows):
            # The first and last row elements are always 1.
            row = [None for _ in range(row_num+1)]
            row[0], row[-1] = 1, 1

            # Each triangle element is equal to the sum of the elements
            # above-and-to-the-left and above-and-to-the-right.
            for j in range(1, len(row)-1):
                row[j] = triangle[row_num-1][j-1] + triangle[row_num-1][j]

            triangle.append(row)

        return triangle
