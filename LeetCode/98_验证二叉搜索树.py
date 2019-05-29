"""给定一个二叉树，判断其是否是一个有效的二叉搜索树。假设一个二叉搜索树具有如下特征：
    节点的左子树只包含小于当前节点的数。  节点的右子树只包含大于当前节点的数。  所有左子树和右子树自身必须也是二叉搜索树。
示例 1:
输入:
    2
   / \
  1   3
输出: true
示例 2:

输入:
    5
   / \
  1   4
     / \
    3   6
输出: false
解释: 输入为: [5,1,4,null,null,3,6]。     根节点的值为 5 ，但是其右子节点值为 4 。
"""
# class TreeNode:             # 给定一个二叉树，判断其是否是一个有效的二叉搜索树
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:             # 二叉搜索树 中序遍历：升序，只用去与前一项比较
    def isValidBST(self, root):     # 递归：指数级复杂度
        res, self.flag = [], True
        self.helper(root, res)
        return self.flag

    def helper(self, root, res):
        if root:
            self.helper(root.left, res)
            if res and root.val <= res[-1]:  # 每个节点都跟前一个节点比较，如果前一个节点比当前节点大的话返回False，否则返回True
                self.flag = False
                return
            res.append(root.val)
            self.helper(root.right, res)
