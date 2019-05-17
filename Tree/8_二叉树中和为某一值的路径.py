"""输入一颗二叉树的跟节点和一个整数，打印出二叉树中结点值的和为输入整数的所有路径。路径定义为从树的根结点开始往下一直到
叶结点所经过的结点形成一条路径。(注意: 在返回值的list中，数组长度大的数组靠前)
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


'''当前节点为叶子节点并和整数值相等时直接输出，当前节点值大于整数值输出空，当前节点值小于整数值，则更新整数值递归下去寻找路径，
注意根节点与递归得到的路径如何合并，没有想好如何解决按路径长度排序输出，直接使用了sorted函数
'''


class Solution:
    # 返回二维列表，内部每个列表表示找到的路径
    def FindPath(self, root, expectNumber):
        if not root or root.val > expectNumber:                 # 空树或根节点值大的情况直接返回
            return []
        if not root.left and not root.right and root.val == expectNumber:
            return [[root.val]]                                 # 叶子节点情况,注意需返回二维list
        else:
            expectNumber -= root.val
            left = self.FindPath(root.left, expectNumber)       # 递归分别求左右子树中的路径     【回溯法】
            right = self.FindPath(root.right, expectNumber)

            result = [[root.val]+x for x in left]               # 与根节点合并     x 是个列表
            for x in right:
                result.append([root.val]+x)
            return sorted(result, key=lambda x: -len(x))        # 输出按路径长度排序的路径列表


class Solution2:
    # 返回二维列表，内部每个列表表示找到的路径
    def FindPath(self, root, expectNumber):
        if not root:
            return []
        if root and not root.left and not root.right and root.val == expectNumber:
            return [[root.val]]
        res = []
        left = self.FindPath(root.left, expectNumber - root.val)
        right = self.FindPath(root.right, expectNumber - root.val)
        for i in left + right:                                  # i 是个列表
            res.append([root.val] + i)                          # '+' 是新建一个列表装下root.val和i两个元素，，"+=":extend
        return sorted(res, key=lambda x: -len(x))               # 输出按路径长度排序的路径列表







