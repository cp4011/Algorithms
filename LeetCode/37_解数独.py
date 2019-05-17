"""编写一个程序，通过已填充的空格来解决数独问题。
一个数独的解法需遵循如下规则：
    数字 1-9 在每一行只能出现一次。  数字 1-9 在每一列只能出现一次。  数字 1-9 在每一个以粗实线分隔的 3x3 宫内只能出现一次。
Note:
给定的数独序列只包含数字 1-9 和字符 '.'（空白格用 '.' 表示）。
你可以假设给定的数独只有唯一解。给定数独永远是 9x9 形式的。
"""


class Solution:
    def solveSudoku(self, board):
        """Do not return anything, modify board in-place instead.   board: List[List[str]]  return: None"""
        '''【回溯法】不停地试数   对于未填数的空位置,从数字1到9去试数,判断该数是否有效（行列块出现相同的数字就不行）'''
        points = []             # 把所有没填数字的位置找到
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    points.append([i, j])

        def check(point, k):        # 检查是否在point位置k是合适的
            row_i, col_j = point[0], point[1]
            for i in range(9):
                if i != row_i and board[i][col_j] == k:                 # 检查 行
                    return False
                if i != col_j and board[row_i][i] == k:                 # 检查 列
                    return False
            for i in range(row_i//3 * 3, row_i//3 * 3 + 3):         # 检查块，如point(7,8),i取6,7,8； j取6,7,8
                for j in range(col_j//3 * 3, col_j//3 * 3 + 3):
                    if i != row_i and j != col_j and board[i][j] == k:  # 检查 该块内3*3 是否有重复
                        return False
            return True

        def backtrack(i=0):
            if i == len(points):                # 回溯终止条件：所有没填的数字全部被填完了
                return True                     # return True 对应语句 if backtrack(i + 1):
            for j in range(1, 10):                  # 填入数字的范围是 1-9
                if check(points[i], str(j)):    # 检查是否合适
                    board[points[i][0]][points[i][1]] = str(j)      # 合适就将数字j填入该位置
                    if backtrack(i + 1):            # 回溯下一个点
                        return True                 # 【如果走到这，则return，表明下面的语句都不会执行了】
                    board[points[i][0]][points[i][1]] = "."         # 不成功则还原为"."，执行到此处则说明上面的语句没有执行到retrun True部分
            return False
        backtrack()
