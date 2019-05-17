"""输入一棵二叉树，求该树的深度。从根结点到叶结点依次经过的结点（含根、叶结点）形成树的一条路径，最长路径的长度为树的深度。"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def TreeDepth(self, pRoot):                 # 【层次遍历】
        if not pRoot:
            return 0
        depth = 0
        queue = [pRoot]                         # queue 用来存储树的每一层的节点，而不是整棵树的节点
        while queue:
            temp = []                           # 用来存储下一层的子节点
            while queue:
                cur = queue.pop(0)
                if cur.left:
                    temp.append(cur.left)
                if cur.right:
                    temp.append(cur.right)
            depth += 1
            queue = temp                        # temp有可能为空，此时while循环结束
        return depth
