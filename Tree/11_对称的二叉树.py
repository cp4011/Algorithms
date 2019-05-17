"""请实现一个函数，用来判断一颗二叉树是不是对称的。注意，如果一个二叉树同此二叉树的镜像是同样的，定义其为对称的。"""
'''首先根节点以及其左右子树，左子树的左子树和右子树的右子树相同,左子树的右子树和右子树的左子树相同即可，采用递归
非递归也可，采用栈或队列存取各级子树根节点'''


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSymmetrical(self, pRoot):

        def is_same(p1, p2):                      # 定义函数
            if not p1 and not p2:                           # 匹配完毕（已经匹配到叶子节点了，且前面的节点都完全匹配）
                return True
            if (p1 and p2) and p1.val == p2.val:            # 当前节点匹配成功，继续调用函数，进行匹配
                return is_same(p1.left, p2.right) and is_same(p1.right, p2.left)
            return False                                    # 除以上所有情况，都为假False

        if not pRoot:
            return True
        if pRoot.left and not pRoot.right or not pRoot.left and pRoot.left:
            return False
        return is_same(pRoot.left, pRoot.right)  # 调用函数
