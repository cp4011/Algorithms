"""二叉搜索树中的两个节点被错误地交换。请在不改变其结构的情况下，恢复这棵树。
示例 1:
输入: [1,3,null,null,2]
   1
  /
 3
  \
   2
输出: [3,1,null,null,2]
   3
  /
 1
  \
   2
示例 2:
输入: [3,1,4,null,null,2]
  3
 / \
1   4
   /
  2
输出: [2,1,4,null,null,3]
  2
 / \
1   4
   /
  3
进阶:使用 O(n) 空间复杂度的解法很容易实现。你能想出一个只使用常数空间的解决方案吗？
"""
"""解题思路：
假设现在有一个乱掉的二叉搜索树[1,2,5,4,3,6,7]。很明显3和5颠倒了。
那么在中序遍历时：当碰到第一个逆序时：为5->4，那么将n1指向5，n2指向4，
注意，此时n1已经确定下来了。然后prev和root一直向后遍历，直到碰到第二个逆序时：4->3，此时将n2指向3，
那么n1和n2都已经确定，只需要交换节点的值即可。prev指针用来比较中序遍历中相邻两个值的大小关系。"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def FindTwoNodes(self, root):           # 中序遍历
        if root:
            self.FindTwoNodes(root.left)
            if self.prev and self.prev.val > root.val:
                self.n2 = root
                if not self.n1:
                    self.n1 = self.prev
            self.prev = root
            self.FindTwoNodes(root.right)

    def recoverTree(self, root):
        """  :type root: TreeNode     :rtype: void Do not return anything, modify root in-place instead.    """
        self.n1 = self.n2 = None
        self.prev = None
        self.FindTwoNodes(root)
        self.n1.val, self.n2.val = self.n2.val, self.n1.val

    # average O(lgn) space (worst case O(n) space), iteratively, one-pass
    def recoverTree1(self, root):
        res, stack, first, second = None, [], None, None
        while True:
            while root:
                stack.append(root)
                root = root.left
            if not stack:
                break
            node = stack.pop()
            # first time occurs reversed order
            if res and res.val > node.val:
                if not first:
                    first = res
                # first or second time occurs reversed order
                second = node
            res = node
            root = node.right
        first.val, second.val = second.val, first.val

    # average O(lgn) space (worst case, O(n) space), recursively, one-pass
    def recoverTree2(self, root):
        self.prevNode = TreeNode(-sys.maxsize - 1)
        self.first, self.second = None, None
        self.inorder(root)
        self.first.val, self.second.val = self.second.val, self.first.val

    def inorder(self, root):
        if not root:
            return
        self.inorder(root.left)
        if not self.first and self.prevNode.val > root.val:
            self.first, self.second = self.prevNode, root
        if self.first and self.prevNode.val > root.val:
            self.second = root
        self.prevNode = root
        self.inorder(root.right)
