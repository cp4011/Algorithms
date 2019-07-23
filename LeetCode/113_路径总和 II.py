"""给定一个二叉树和一个目标和，找到所有从根节点到叶子节点路径总和等于给定目标和的路径。
说明: 叶子节点是指没有子节点的节点。
示例:    给定如下二叉树，以及目标和 sum = 22，
              5
             / \
            4   8
           /   / \
          11  13  4
         /  \    / \
        7    2  5   1
返回:
[
   [5,4,11,2],
   [5,8,4,5]
]
"""


def pathSum(root, sum):     # 给定一个二叉树和一个目标和，找到所有从根节点到叶子节点路径总和等于给定目标和的路径
    if not root:
        return []
    res = []

    def helper(root, sum, tmp):
        if not root:
            return
        if not root.left and not root.right and sum - root.val == 0:
            tmp += [root.val]
            res.append(tmp)
            return
        helper(root.left, sum - root.val, tmp + [root.val])
        helper(root.right, sum - root.val, tmp + [root.val])

    helper(root, sum, [])
    return res
