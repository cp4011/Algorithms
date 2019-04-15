"""二叉树的创建 + 遍历"""


class Node(object):
    """二叉树节点"""
    def __init__(self, elem=-1, lchild=None, rchild=None):
        self.elem = elem
        self.lchild = lchild
        self.rchild = rchild


class Tree(object):
    """二叉树"""
    def __init__(self, root=None):
        self.root = root

    def add(self, elem):                    # 构建二叉树的节点：用【队列】存放上层的树节点
        """为树添加节点"""
        node = Node(elem)
        if self.root == None:               # 如果树是空的，则对根节点赋值
            self.root = node
        else:
            queue = list()
            queue.append(self.root)
            while queue:
                cur = queue.pop(0)          # 弹出队列的第一个元素
                if cur.lchild == None:
                    cur.lchild = node
                    return
                elif cur.rchild == None:
                    cur.rchild = node
                    return
                else:                       # 如果左右子树都不为空，往判断列表加入子树，循环进行子树的判断
                    queue.append(cur.lchild)
                    queue.append(cur.rchild)


    '''树先中后序遍历（深度优先遍历）'''

    def preorder(self, root):
        """递归实现先序遍历"""
        if root == None:
            return                          # return 与return None相同，返回值为None
        print(root.elem)
        self.preorder(root.lchild)
        self.preorder(root.rchild)

    def inorder(self, root):
        """递归实现中序遍历"""
        if root == None:
            return
        self.inorder(root.lchild)
        print(root.elem)
        self.inorder(root.rchild)

    def postorder(self, root):
        """递归实现后续遍历"""
        if root == None:
            return
        self.postorder(root.lchild)
        self.postorder(root.rchild)
        print(root.elem)

    '''利用队列实现树的【层次遍历】(广度优先遍历）'''
    def breadth_travel(self, root):
        if root == None:
            return
        queue = list()
        queue.append(root)
        while queue:
            node = queue.pop(0)
            print(node.elem)
            if node.lchild != None:
                queue.append(node.lchild)
            if node.rchild != None:
                queue.append(node.rchild)

