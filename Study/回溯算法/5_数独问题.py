class Solution:
    def solveSudoku(self, board):
        self.helper(board, 0)                               # index从0开始（第一格）

    def helper(self, board, index):
        if index >= 81:                                     # 如果盘面已满
            self.printSolution(board)                       # 输出结果
            return                                          # 返回上一格（可能有多解，继续求解）
        if board[index] == 0:                               # 如果当前格为空格
            for i in range(1, 10):                          # 依次假设1-9
                if self.isValid(board, index, i):           # 如果假设成立
                    board[index] = i                        # 填入数字
                    self.helper(board, index + 1)           # 继续假设
                    board[index] = 0                        # 将格子改回空格，以便继续假设其他数字【当前假设的数字i不成立或者已经输出了结果】
        else:                                               # 如果当前格有已知数
            self.helper(board, index + 1)                   # 格子不为空，则跳过此格

    def printSolution(self, board): 			            # 输出结果
        for i in range(0, 81, 9):
            print(board[i:i+9])

    def isValid(self, board, index, num):	                # isValid方法检查当前假设是否合理
        row = index // 9				                    # 当前格子的行数
        column = index % 9				                    # 当前格子的列数
        for i in range(index + 9, 81, 9):	                # 检查和同列（下方）的格子是否矛盾
            if board[i] == num:
                return False
        for i in range(index - 9, -1, -9):                  # 检查和同列（上方）的格子是否矛盾
            if board[i] == num:
                return False
        for i in range(9 * row, 9 * (row + 1)):	            # 检查和同行的格子是否矛盾
            if board[i] == num:
                return False
        for i in range(row - row % 3, 3 + row - row % 3):   # 检查和同粗线格的格子是否矛盾
            for j in range(column - column % 3, 3 + column - column % 3):
                if board[j + i * 9] == num:
                    return False
        return True


Solution().solveSudoku([4,1,0,0,0,7,8,5,0,\
                        8,0,6,0,0,0,0,0,9,\
                        0,2,0,0,9,0,6,0,0,\
                        0,0,4,0,0,0,0,1,2,\
                        2,0,0,5,8,0,0,7,0,\
                        0,0,0,0,0,0,5,0,0,\
                        0,0,0,7,0,2,0,0,0,\
                        0,0,8,0,1,0,0,0,0,\
                        0,7,0,0,6,0,0,0,0])


"""编写一个程序，通过已填充的空格来解决数独问题。一个数独的解法需遵循如下规则：
数字 1-9 在每一行只能出现一次。
数字 1-9 在每一列只能出现一次。
数字 1-9 在每一个以粗实线分隔的 3x3 宫内只能出现一次。
空白格用 '.' 表示。
"""


# 回溯算法
class Solution:
    # @param board, a 9x9 2D array
    # Solve the Sudoku by modifying the input board in-place.
    # Do not return any value.
    def solveSudoku(self, board):
        self.board = board
        self.solve()

    def findUnassigned(self):
        for row in range(9):
            for col in range(9):
                if self.board[row][col] == ".":
                    return row, col
        return -1, -1

    def solve(self):
        row, col = self.findUnassigned()
        # no unassigned position is found, puzzle solved
        if row == -1 and col == -1:
            return True
        for num in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            if self.isSafe(row, col, num):
                self.board[row][col] = num
                if self.solve():
                    return True
                self.board[row][col] = "."
        return False

    def isSafe(self, row, col, ch):
        boxrow = row - row % 3
        boxcol = col - col % 3
        if self.checkrow(row, ch) and self.checkcol(col, ch) and self.checksquare(boxrow, boxcol, ch):
            return True
        return False

    def checkrow(self, row, ch):
        for col in range(9):
            if self.board[row][col] == ch:
                return False
        return True

    def checkcol(self, col, ch):
        for row in range(9):
            if self.board[row][col] == ch:
                return False
        return True

    def checksquare(self, row, col, ch):
        for r in range(row, row + 3):
            for c in range(col, col + 3):
                if self.board[r][c] == ch:
                    return False
        return True

