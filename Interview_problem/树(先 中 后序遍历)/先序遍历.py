# 前序遍历
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root == None:
            return []
        resLs = []
        stack, node = [], root
        while stack.__len__() > 0 or node != None:
            while node != None:
                resLs.append(node.val)
                stack.append(node)
                node = node.left
            node = stack.pop()
            node = node.right
        return resLs

