"""在8×8格的国际象棋上摆放八个皇后，使其不能互相攻击，即任意两个皇后都不能处于同一行、同一列或同一斜线上，问有多少种摆法"""


class Solution(object):

    def solveNQueens(self, n):
        self.helper([-1] * n, 0, n)                  # 初始化columnPositions列表中的值全为-1，从第0行开始到底n-1行

    def helper(self, columnPositions, rowIndex, n):  # columnPositions:存储保安位置的列表,数字下标代表第几行,存储的值代表第几列。rowIndex当前行数.n皇后的个数
        if rowIndex == n:                                           # rowIndex代表当前行，n皇后个数
            self.printSolution(columnPositions, n)                  # 如果走完了所有行就输出结果
            return                                                  # 返回到上一行的假设
        for column in range(n):
            columnPositions[rowIndex] = column                      # 假设第rowIndex行的保安位置【列】
            if self.isValid(columnPositions, rowIndex):             # 如果可行，isValid方法检查位置是否合理
                self.helper(columnPositions, rowIndex + 1, n)       # 继续假设剩余行的保安位置

    def isValid(self, columnPositions, rowIndex):                   # isValid方法检查位置是否合理
        for i in range(rowIndex):
            if columnPositions[i] == columnPositions[rowIndex]:     # 检查同列是否有保安
                return False
            elif abs(columnPositions[i] - columnPositions[rowIndex]) == rowIndex - i:
                return False                                        # 检查两条斜线上是否有保安【|列之差|=|行之差|】
        return True

    def printSolution(self, columnPositions, n):                    # printSolution方法输出打印结果
        for row in range(n):
            line = ""
            for column in range(n):
                if columnPositions[row] == column:
                    line += "Q "
                else:
                    line += ". "
            print(line[:-1])
        print("\n")


Solution().solveNQueens(8)                                          # 调用solveNQueens解决8皇后问题


