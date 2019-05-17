"""输入一棵二叉树，判断该二叉树是否是平衡二叉树。"""

'''后续遍历时，遍历到一个节点，其左右子树已经遍历  依次自底向上判断，每个节点只需要遍历一次'''

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def IsBalanced_Solution(self, pRoot):
        return self.balanceHeight(pRoot) >= 0

    def balanceHeight(self, root):
        if root is None:
            return 0
        left = self.balanceHeight(root.left)
        right = self.balanceHeight(root.right)

        if left < 0 or right < 0 or abs(left - right) > 1:
            return -1
        return max(left, right) + 1
