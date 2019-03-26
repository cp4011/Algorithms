# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root == None:
            return []
        stack, node = [], root
        resLs = []
        while stack.__len__() > 0 or node != None:
            while node != None:  ###向左叶子节点遍历直到最底层
                stack.append(node)
                node = node.left
            node = stack.pop()
            resLs.append(node.val)
            node = node.right
        return resLs
