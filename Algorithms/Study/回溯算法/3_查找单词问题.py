class Solution:
    def wordSearch(self, board, word):
        for i in range(len(board)):
            for j in range(len(board[0])):                                      # 遍历盘面
                if self.helper(board, word, i, j):		                        # 调用helper方法
                    return True
        return False

    def helper(self, board, current, row, column):			                    # helper方法（回溯方法），该函数返回 布尔值
        if len(current) == 0:							                        # 结束条件
            return True
        if row >= 0 and row < len(board) and column >= 0 and column < len(board[0]):    # 前提条件
            if board[row][column] == current[0]:			                            # 如果两个字母对应剩余单词首字母
                board[row][column] = ""                                                 # 把该字母从盘面中去除，以免二次利用
                if self.helper(board, current[1:], row-1, column):	                    # 上下左右检查剩余字母，上
                    return True
                if self.helper(board, current[1:], row+1, column):                      # 下
                    return True
                if self.helper(board, current[1:], row, column-1):                      # 左
                    return True
                if self.helper(board, current[1:], row, column+1):                      # 右
                    return True
                board[row][column] = current[0]                         # 若前4个方法没有return，将会执行本行代码，将字母填回盘面上
        return False


board = [['a', 'c', 'r', 'y', 'l'],
         ['l', 'w', 'o', 'r', 'i'],
         ['a', 'f', 'd', 'l', 'c'],
         ['k', 'e', 'e', 'w', 'e'],
         ['o', 'd', 'r', 'o', 's']]
print(Solution().wordSearch(board, "week"))
