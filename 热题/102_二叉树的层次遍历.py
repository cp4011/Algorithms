"""给定一个二叉树，返回其按层次遍历的节点值。 （即逐层地，从左到右访问所有节点）。
例如: 给定二叉树: [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
返回其层次遍历结果：
[
  [3],
  [9,20],
  [15,7]
]
"""


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def levelOrder(self, root):
        if not root:
            return []
        res, queue = [], [root]
        while queue:
            line, next_line = [], []        # 注意这行的位置不是在第二个循环中
            while queue:
                node = queue.pop(0)
                line.append(node.val)
                if node.left:
                    next_line.append(node.left)
                if node.right:
                    next_line.append(node.right)
            queue = next_line
            res.append(line)
        return res

