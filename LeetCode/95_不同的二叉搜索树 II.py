"""给定一个整数 n，生成所有由 1 ... n 为节点所组成的二叉搜索树。
示例: 输入: 3
输出:
[  [1,null,3,2],
  [3,2,null,1],
  [3,1,null,null,2],
  [2,1,3],
  [1,null,2,null,3] ]
解释:以上的输出对应以下 5 种不同结构的二叉搜索树：
   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def generateTrees(self, n):
        def helper(x, y):
            if x > y: return [None]
            if x == y: return [TreeNode(x)]

            ans = []
            for v in range(x, y + 1):
                lans = helper(x, v - 1)
                rans = helper(v + 1, y)

                for l in lans:
                    for r in rans:
                        root = TreeNode(v)
                        root.left = l
                        root.right = r
                        ans.append(root)
            return ans

        return helper(1, n) if n >= 1 else []
