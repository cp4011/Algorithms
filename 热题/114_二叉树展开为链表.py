"""给定一个二叉树，原地将它展开为链表。
例如，给定二叉树

    1
   / \
  2   5
 / \   \
3   4   6
将其展开为：
1
 \
  2
   \
    3
     \
      4
       \
        5
         \
          6
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def flatten(self, root: TreeNode) -> None:
        """ Do not return anything, modify root in-place instead.
                1
               / \
              2   5
             / \   \
            3   4   6
        """
        while (root != None):
            if root.left != None:           # 节点2
                most_right = root.left      # 如果左子树不为空, 那么就先找到左子树的最右节点（节点4）
                while most_right.right != None: most_right = most_right.right   # 找最右节点（节点4）
                most_right.right = root.right       # 然后将根的右孩子放到最右节点的右子树上（节点4的右节点  指向 节点5以及所在的树）
                root.right = root.left  # 这时候根的右孩子可以释放, 因此可令 根的左孩子 移动到 根的右孩子上
                root.left = None        # 将左孩子置为空
            root = root.right       # 继续下一个节点
        return

