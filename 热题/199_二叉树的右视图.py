"""给定一棵二叉树，想象自己站在它的右侧，按照从顶部到底部的顺序，返回从右侧所能看到的节点值。
示例:
输入: [1,2,3,null,5,null,4]
输出: [1, 3, 4]
解释:

   1            <---
 /   \
2     3         <---
 \     \
  5     4       <---
"""


# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rightSideView(self, root):      # 层次遍历 取每一层的最后一个节点
        if not root:
            return []
        res = []
        queue = [root]
        while queue:
            line = []
            next_line = []
            while queue:
                node = queue.pop(0)
                line.append(node)
                if node.left:
                    next_line.append(node.left)
                if node.right:
                    next_line.append(node.right)
            res.append(line[-1].val)
            queue = next_line
        return res

    def rightSideView_deque(self, root):
        from collections import deque
        if not root:
            return []
        res = []
        queue = deque([root])       # deque([iterable[, maxlen]])
        while queue:
            line = []
            next_line = deque([])
            while queue:
                node = queue.popleft()
                line.append(node)
                if node.left:
                    next_line.append(node.left)
                if node.right:
                    next_line.append(node.right)
            res.append(line[-1].val)
            queue = next_line
        return res
