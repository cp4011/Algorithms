"""给定一个二叉树，检查它是否是镜像对称的。
例如，二叉树 [1,2,2,3,4,4,3] 是对称的。
    1
   / \
  2   2
 / \ / \
3  4 4  3
但是下面这个 [1,2,2,null,3,null,3] 则不是镜像对称的:
    1
   / \
  2   2
   \   \
   3    3
说明: 如果你可以运用递归和迭代两种方法解决这个问题，会很加分。
"""


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def func(l, r):
            if not l and not r:
                return True
            if l and r and l.val == r.val:
                return func(l.left, r.right) and func(l.right, r.left)
            return False

        if not root:
            return True
        return func(root.left, root.right)
