"""请设计一个函数，用来判断在一个矩阵中是否存在一条包含某字符串所有字符的路径。路径可以从矩阵中的任意一个格子开始，每一步
可以在矩阵中向左，向右，向上，向下移动一个格子。如果一条路径经过了矩阵中的某一个格子，则之后不能再次进入这个格子。
例如 a b c e s f c s a d e e 这样的3 X 4 矩阵中包含一条字符串"bcced"的路径，但是矩阵中不包含"abcb"路径，因为字符串的第一个
字符b占据了矩阵中的第一行第二个格子之后，路径不能再次进入该格子。
"""

'''回朔法解决的典型题
    首先，在矩阵中任选一个格子作为路径的起点。如果路径上的第i个字符不是ch，那么这个格子不可能处在路径上的第i个位置。如果
路径上的第i个字符正好是ch，那么往相邻的格子寻找路径上的第i+1个字符。除在矩阵边界上的格子之外，其他格子都有4个相邻的格子。
重复这个过程直到路径上的所有字符都在矩阵中找到相应的位置。
　　由于回朔法的递归特性，路径可以被开成一个栈。当在矩阵中定位了路径中前n个字符的位置之后，在与第n个字符对应的格子的周围都没有找到第n+1个
字符，这个时候只要在路径上回到第n-1个字符，重新定位第n个字符。
　　由于路径不能重复进入矩阵的格子，还需要定义和字符矩阵大小一样的布尔值矩阵，用来标识路径是否已经进入每个格子。 当矩阵中坐标为（row,col）的
格子和路径字符串中相应的字符一样时，从4个相邻的格子(row,col-1),(row-1,col),(row,col+1)以及(row+1,col)中去定位路径字符串中下一个字符
如果4个相邻的格子都没有匹配字符串中下一个的字符，表明当前路径字符串中字符在矩阵中的定位不正确，我们需要回到前一个，然后重新定位。
　　一直重复这个过程，直到路径字符串上所有字符都在矩阵中找到合适的位置
'''

'''回溯:
    0.根据给定数组，初始化一个标志位数组，初始化为false，表示未走过，true表示已经走过，不能走第二次
    1.根据行数和列数，遍历数组，先找到一个与str字符串的第一个元素相匹配的矩阵元素，进入judge
    2.根据i和j先确定一维数组的位置，因为给定的matrix是一个一维数组
    3.确定递归终止条件：越界，当前找到的矩阵值不等于数组对应位置的值，已经走过的，这三类情况，都直接false，说明这条路不通
    4.若k，就是待判定的字符串str的索引已经判断到了最后一位，此时说明是匹配成功的
    5.下面就是本题的精髓，递归不断地寻找周围四个格子是否符合条件，只要有一个格子符合条件，就继续再找这个符合条件的格子的
四周是否存在符合条件的格子，直到k到达末尾或者不满足递归条件就停止。
    6.走到这一步，说明本次是不成功的，我们要还原一下标志位数组index处的标志位，进入下一轮的判断。
'''


# 回溯法【遍历矩阵中的每一个位置】
# 【matrix[i * cols + j]】  若处理成矩阵：x = [list(matrix[cols*i:cols*i+cols]) for i in range(rows)]     if matrix[i][j] == p[0]
class Solution:
    def hasPath(self, matrix, rows, cols, path):
        if not matrix:
            return False
        if not path:
            return True
        for i in range(rows):
            for j in range(cols):
                if self.helper(list(matrix), rows, cols, path, i, j):           # 必须list变成列表，因为python的string是不可以被修改的
                    return True
        return False

    def helper(self, matrix, rows, cols, path, i, j):
        if matrix[i * cols + j] == path[0]:                 # 注意是i * cols 列，，而不是行rows。【i * cols + j】
            if not path[1:]:
                return True
            matrix[i * cols + j] = '0'                                          # 修改已经遍历过的字母（前提是字符串已经转成了列表）
            if i - 1 >= 0 and self.helper(matrix, rows, cols, path[1:], i - 1, j):          # 上
                return True
            if i + 1 < rows and self.helper(matrix, rows, cols, path[1:], i + 1, j):        # 下
                return True
            if j - 1 >= 0 and self.helper(matrix, rows, cols, path[1:], i, j - 1):          # 左
                return True
            if j + 1 < cols and self.helper(matrix, rows, cols, path[1:], i, j + 1):        # 右
                return True
            matrix[i * cols + j] = path[0]        # 遍历完上下左右后，仍然没找到第二个字母，则将第一个字母还原
            return False
        return False


class Solution1:
    def hasPath(self, matrix, rows, cols, path):
        if not matrix or rows < 1 or cols < 1 or not path:
            return False

        visited = [0] * (rows * cols)
        pathLength = 0
        for r in range(rows):
            for c in range(cols):
                if self.hasPathCore(matrix, rows, cols, r, c, path, pathLength, visited):
                    return True
        return False

    def hasPathCore(self, matrix, rows, cols, r, c, path, pathLength, visited):
        if pathLength == len(path):
            return True

        flag = False

        if r >= 0 and r < rows and c >= 0 and c < cols and matrix[r * cols + c] == path[pathLength] and not visited[r * cols + c]:
            pathLength += 1
            visited[r * cols + c] = True

            flag = self.hasPathCore(matrix, rows, cols, r, c - 1, path, pathLength, visited) \
                   or self.hasPathCore(matrix, rows, cols, r - 1, c, path, pathLength, visited) \
                   or self.hasPathCore(matrix, rows, cols, r, c + 1, path, pathLength, visited) \
                   or self.hasPathCore(matrix, rows, cols, r + 1, c, path, pathLength, visited)

            if not flag:
                pathLength -= 1
                visited[r * cols + c] = False
        return flag
