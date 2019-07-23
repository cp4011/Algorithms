"""给定一个二叉树, 找到该树中两个指定节点的最近公共祖先。
百度百科中最近公共祖先的定义为：“对于有根树 T 的两个结点 p、q，最近公共祖先表示为一个结点 x，满足 x 是 p、q 的祖先且 x
的深度尽可能大（一个节点也可以是它自己的祖先）。”
例如，给定如下二叉树:  root = [3,5,1,6,2,0,8,null,null,7,4]

示例 1:
输入: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
输出: 3
解释: 节点 5 和节点 1 的最近公共祖先是节点 3。
示例 2:
输入: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
输出: 5
解释: 节点 5 和节点 4 的最近公共祖先是节点 5。因为根据定义最近公共祖先节点可以为节点本身。
 
说明:     所有节点的值都是唯一的。    p、q 为不同节点且均存在于给定的二叉树中。
"""

'''思路：由于要求深度尽可能大，因此分三种情况，一是p、q两个值分别在二叉树根节点两侧，二是同在左子树，三是同在右子树，因此
最大根节点问题转化成搜索问题，搜索p、q（唯一）两个值分别在哪
'''


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def lowestCommonAncestor(self, root, p, q):     # 给定一个二叉树, 找到该树中两个指定节点的最近公共祖先
        """    :type root: TreeNode        :type p: TreeNode        :type q: TreeNode        :rtype: TreeNode    """
        if root is None or root == p or root == q:
            return root     # 若root为空或者root为p或者root为q，说明找到了p和q其中一个
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if left and right:
            return root     # 若左子树找到了p，右子树找到了q，说明此时的root就是公共祖先
        if not left:
            return right    # 若左子树是none而右子树不是，说明右子树找到了p或q
        if not right:
            return left
        return None
