"""给定一个非空二叉树，返回其最大路径和。
本题中，路径被定义为一条从树中任意节点出发，达到任意节点的序列。该路径至少包含一个节点，且不一定经过根节点。
示例 1:
输入: [1,2,3]
       1
      / \
     2   3
输出: 6
示例 2:
输入: [-10,9,20,null,null,15,7]
   -10
   / \
  9  20
    /  \
   15   7
输出: 42
"""
class Solution:
    def maxPathSum(self, root):

        def max_gain(node):  # 在每一步都检查哪种选择更好：是继续当前路径（一条斜线的路径）？ 或者 以当前节点作为最高节点计算新的路径（三角形的新路径）？
            # nonlocal max_sum  # 定义max_sum为外层函数的一个局部变量（如果外层不是一个函数，而是全局变量，则用global）
            if not node:
                return 0

            left_gain = max(max_gain(node.left), 0)  # 左右子树的最大路径和
            right_gain = max(max_gain(node.right), 0)

            price_newpath = node.val + left_gain + right_gain  # 以node为最高节点的新路径的最大路径和（三角形的新路径）
            self.max_sum = max(self.max_sum, price_newpath)  # 将新路径和与旧路径比较，更新最大路径和

            return node.val + max(left_gain, right_gain)  # 递归 返回当前节点的一条最大路径（一条斜线的路径）

        self.max_sum = float('-inf')
        max_gain(root)
        return self.max_sum


''' python 的 global 和 nonlocal 区别
    两个关键词都用于允许在一个局部作用域中使用外层的变量。

        global 表示将变量声明为全局变量 （ global  a 
                                            a = 3 # 定义全局变量）
        nonlocal 表示将变量声明为外层变量（外层函数的局部变量，而且不能是全局变量）

        ##原理
                1、 python 在访问一个变量时，先要去定位这个变量来源于哪里。
                python引用变量的顺序如下：
                当前作用域局部变量
                外层作用域变量
                当前模块中的全局变量
                python内置变量
                即优先从局部作用域中查找这个变量，如果没有的话，再去外层找，如果到了最后还没找到，则报错。
'''