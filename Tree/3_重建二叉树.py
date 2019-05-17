"""输入某二叉树的前序遍历和中序遍历的结果，请重建出该二叉树。假设输入的前序遍历和中序遍历的结果中都不含重复的数字。例如
输入前序遍历序列{1,2,4,7,3,5,6,8}和中序遍历序列{4,7,2,1,5,3,8,6}，则重建二叉树并返回。
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def reConstructBinaryTree(self, pre, tin):          # 返回构造的TreeNode根节点
        if len(pre) == 0:                               # 递归结束条件
            return None
        root = TreeNode(pre[0])                         # 根root
        pos = tin.index(pre[0])
        root.left = self.reConstructBinaryTree(pre[1:pos+1], tin[0:pos])        # 左子树  【注意在class中要有self】
        root.right = self.reConstructBinaryTree(pre[pos+1:], tin[pos+1:])       # 右子树
        return root                                                             # 返回

