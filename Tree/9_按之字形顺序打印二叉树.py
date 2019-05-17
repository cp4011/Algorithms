"""请实现一个函数按照之字形打印二叉树，即第一行按照从左到右的顺序打印，第二层按照从右至左的顺序打印，第三行按照从左到右
的顺序打印，其他行以此类推。
"""
'''用例:{5,#,4,#,3,#,2}
对应输出应该为: [[5],[4],[3],[2]]
'''


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def Print(self, pRoot):
        if not pRoot:
            return []
        queue = [pRoot]                     # 树的一层节点队列
        level = 1
        res = []

        while queue:
            this_line = []                  # 当前层
            next_line = []                  # 记录下一层的子节点
            for cur in queue:               # 遍历当前层的所有节点
                this_line.append(cur.val)
                if cur.left:
                    next_line.append(cur.left)
                if cur.right:
                    next_line.append(cur.right)
            if level % 2 == 0:              # 树的偶数层时，反转列表
                this_line.reverse()
            res.append(this_line)           # 加入结果列表中
            queue = next_line               # 将下一层的子节点列表赋值给queue
            level += 1                      # 层数+1
        return res
