"""给定一个二叉树，返回它的 中序 遍历。
示例:
输入: [1,null,2,3]
   1
    \
     2
    /
   3

输出: [1,3,2]
进阶: 递归算法很简单，你可以通过迭代算法完成吗？
"""


class Solution:     # 中序遍历需要最先访问左孩子，因此需要一直遍历到左孩子结点为空的结点才进行访问，然后再访问右孩子。
    def inorderTraversal(self, root):
        if not root:
            return []       # 返回 []
        stack = []
        res = []
        while stack or root:
            while root:
                stack.append(root)
                root = root.left    # 先访问左孩子,一直遍历到左孩子结点为空的结点
            if stack:
                root = stack.pop()
                res.append(root.val)
                root = root.right   # 然后再访问右孩子
        return res

    def inorderTraversal1(self, root):
        def inorder(root):
            if not root:
                return
            inorder(root.left)
            ans.append(root.val)
            inorder(root.right)
        ans = []
        inorder(root)
        return ans

