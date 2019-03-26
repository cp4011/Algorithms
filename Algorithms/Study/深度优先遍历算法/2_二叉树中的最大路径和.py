"""LeetCode 124
给定一个非空二叉树，返回其最大路径和。
本题中，路径被定义为一条从树中任意节点出发，达到任意节点的序列。该路径至少包含一个节点，且不一定经过根节点。
示例 1:
输入: [1,2,3]
       1
      / \
     2   3

输出: 6
示例 2:
输入: [-10,9,20,null,null,15,7]
   -10
   / \
  9  20
    /  \
   15   7
输出: 42
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxPathSum(self, root):                     # 输出最大路径和的方法
        return max(self.helper(root))               # 调用helper方法，传入根节点，输出返回的两个值的最大值

    def helper(self, root):                         # helper方法，输出一个二维数组 [ 不停值，停值 ]
        if root == None:                                                            # 如果节点为空，输出两个最小值
            return float('-int'), float('-int')
        leftY, leftN = self.helper(root.left)                                       # 得到左子节点的不停值与停值
        rightY, rightN = self.helper(root.right)                                    # 得到右子节点的不停值与停值
        yes = max(root.val + leftY, root.val + rightY, root.val)  # 不停值
        no = max(leftN, rightN, leftY, rightY, root.val + leftY + rightY)           # 停值
        return yes, no                                                              # 输出 [ 不停值，停值 ]


class Solution:
    def maxPathSum(self, root):
        '''
        the maxPath is the maximum of all path passing through the root node for all the subtrees, including the tree itself.
        So we need to calculate the maximum of the path passing through the node. And take the maximum of those path for all subtrees.
        To calculate the maximum path sum passing through node, we calculate the maximum path sum from the root.
        We use the maximum path sum from root of the subtree and root.val to construct the maximum path sum passing through the node
        '''
        self.ans = -999999999
        self._maxPathSumFromRoot(root)
        return self.ans

    def _maxPathSumFromRoot(self, root):
        res = 0
        if not root:
            return res
        res = root.val
        ans = root.val
        left = self._maxPathSumFromRoot(root.left)
        right = self._maxPathSumFromRoot(root.right)
        res = root.val + max(left, right, 0)
        if left > 0:
            ans += left
        if right > 0:
            ans += right
        self.ans = max(self.ans, ans)
        return res
