""" 遍历树的方式有前序遍历、中序遍历、后序遍历以及层序遍历四种
        前序遍历： 根、左、右
        中序遍历：左、根、右
        后序遍历：左、右、根
"""


def preOrder(root):
    if not root:
        return []
    stack = [root]
    res = []
    while stack:
        root = stack.pop()
        res.append(root.val)
        if root.right:
            stack.append(root.right)
        if root.left:
            stack.append(root.left)
    return res


# 由于中序遍历需要最先访问左孩子，因此需要一直遍历到左孩子结点为空的结点才进行访问，然后再访问右孩子。
def inOrder(root):
    if not root:
        return []
    stack = []
    res = []
    while stack or root:
        while root:
            stack.append(root)
            root = root.left
        if stack:
            root = stack.pop()
            res.append(root.val)
            root = root.right
    return res


# 这里采用相反的方式，先访问根节点，再来是右孩子，最后左孩子。这样遍历完之后返回遍历结果的倒序，即是最终的结果。
def postOrder(root):
    if not root:
        return []
    stack = []
    res = []
    while stack or root:
        while root:
            stack.append(root)
            res.append(root.val)
            root = root.right
        if stack:
            root = stack.pop()
            root = root.left
    return res[::-1]
# 【层序遍历】用到队列，当左孩子存在，则入队，右孩子存在，入队，每次取队首结点。
def levelOrder(root):
    if not root:
        return []
    queue = [root]
    res = []
    while queue:
        root = queue[0]
        queue = queue[1:]
        res.append(root.val)
        if root.left:
            queue.append(root.left)
        if root.right:
            queue.append(root.right)
    return res
