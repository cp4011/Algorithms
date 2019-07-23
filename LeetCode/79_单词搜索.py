"""给定一个二维网格和一个单词，找出该单词是否存在于网格中。
单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的
字母不允许被重复使用。
示例:
board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]
给定 word = "ABCCED", 返回 true.
给定 word = "SEE", 返回 true.
给定 word = "ABCB", 返回 false.
"""


class Solution:
    def exist(self, board, word):       # 给定一个二维网格和一个单词，找出该单词是否存在于网格中(单词必须按照字母顺序)
        if not board:
            return False
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.dfs(board, i, j, word):
                    return True
        return False

    def dfs(self, board, i, j, word):   # 从(i,j)开始查找，返回是否找到该单词的布尔值
        if len(word) == 0:              # 该单词的所有字母都已经被按照字母的顺序给找到了
            return True
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or word[0] != board[i][j]:
            return False
        tmp = board[i][j]               # 第一个字母都找到了，继续查找单词剩余的部分
        board[i][j] = "#"               # 修改元素，避免被重复访问
        # 从四个方向继续查找下一个字母
        res = self.dfs(board, i+1, j, word[1:]) or self.dfs(board, i-1, j, word[1:]) \
        or self.dfs(board, i, j+1, word[1:]) or self.dfs(board, i, j-1, word[1:])
        board[i][j] = tmp               # 从(i,j)开始查找了所有顺序方向，也没有找到，则将修改了的元素填回
        return res                      # 返回res的布尔值
