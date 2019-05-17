"""给定一棵二叉搜索树，请找出其中的第k小的结点。例如，（5，3，7，2，4，6，8）中，按结点数值大小顺序第三小结点的值为4。"""

'''【二叉搜索树】 按照 【中序遍历】就是升序排列的数组'''
# 第三个节点是4,前序遍历5324768,中序遍历2345678,后序遍历2436875,所以是中序遍历，左根右


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def KthNode(self, pRoot, k):
        global res                                  # 定义global变量res
        res = []                                    # 初始化
        self.inorder(pRoot)
        if k <= 0 or k > len(res):                  # 注意是 【or】
            return
        return res[k-1]

    def inorder(self, root):                        # 中序遍历（递归），函数外定义了一个global全局变量res 来存储遍历的各结点
        if not root:
            return
        self.inorder(root.left)
        res.append(root)                            # 注意存储的是节点，而不是节点的值val
        self.inorder(root.right)


class Solution2:
    def KthNode(self, pRoot, k):
        if not pRoot or k < 1:
            return None
        buf = []
        if len(self.inorder(pRoot, buf)) < k:
            return None
        return self.inorder(pRoot, buf)[k - 1]

    def inorder(self, pRoot, buf):
        if not pRoot:
            return None
        self.inorder(pRoot.left, buf)
        buf.append(pRoot)
        self.inorder(pRoot.right, buf)
        return buf
