#-*- coding:utf-8 -*-
class Node:
    def __init__(self,data):
        self.data=data
        self.lchild=None
        self.rchild=None

class Tree:
    def __init__(self):
        self.queue=[]#利用队列存储树的节点
        self.flag=0#存储树根后flag置为1
        self.root=None

    #建树
    def createTree(self,list):
        while True:
            #list中没有数据，表示建树完成
            if len(list)==0:
                return
            #flag为0，表示树根不存在
            if self.flag==0:
                self.root=Node(list[0])
                #讲树根存入队列
                self.queue.append(self.root)
                #树根已创建，flag置为1
                self.flag=1
                #剔除list中第一个已经使用数
                list.pop(0)
            else:
                '''
                treeNode:队列中的第一个节点(该节点左右孩子不完全存在)
                添加treeNode的左右孩子，当添加treeNode的右孩子之后，
                将队列中的第一个节点出队。
                '''
                treeNode=self.queue[0]
                if treeNode.lchild==None:
                    treeNode.lchild=Node(list[0])
                    self.queue.append(treeNode.lchild)
                    list.pop(0)
                else:
                    treeNode.rchild = Node(list[0])
                    self.queue.append(treeNode.rchild)
                    list.pop(0)
                    self.queue.pop(0)


    # 递归实现先序遍历
    def front_digui(self,root):
        if root==None:
            return
        else:
            print(root.data)
            self.front_digui(root.lchild)
            self.front_digui(root.rchild)
    # 递归实现中序遍历
    def middle_digui(self,root):
        if root==None:
            return
        else:
            self.middle_digui(root.lchild)
            print(root.data)
            self.middle_digui(root.rchild)
    # 递归实现后序遍历
    def behind_digui(self,root):
        if root==None:
            return
        else:
            self.behind_digui(root.lchild)
            self.behind_digui(root.rchild)
            print(root.data)

    # 队栈实现先序遍历
    def front_queueAndStack(self,root):
        if root==None:
            return
        #定义一个栈,存储节点
        stack=[]
        node=root
        while stack or node:
            #从树根开始一直输出左孩子
            while node:
                print(node.data)
                #将输出的节点加入栈中
                stack.append(node)
                node=node.lchild
            #该节点不存在左节点时,该节点出栈,搜索该节点右节点，
            node=stack.pop()
            node=node.rchild
    # 队栈实现中序遍历
    def middle_queueAndStack(self,root):
        if root==None:
            return
        # 定义一个栈,存储节点
        stack = []
        node = root
        while stack or node:
            #一直查找树的左节点,一直进栈
            while node:
                stack.append(node)
                node=node.lchild
            node=stack.pop()#该节点不存在左节点，该节点出栈，查找右节点
            print(node.data)
            node=node.rchild
    # 队栈实现后序遍历
    def behind_queueAndStack(self,root):
        if root==None:
            return
        # 定义一个栈,存储节点
        stack_1 = []
        stack_2 = []
        node = root
        stack_1.append(node)
        while stack_1:
            #该节点出栈1.左右节点进栈1(对于左右节点,右节点先出栈1,也先进栈1)
            node=stack_1.pop()
            if node.lchild:
                stack_1.append(node.lchild)
            if node.rchild:
                stack_1.append(node.rchild)
            #该节点进栈2
            stack_2.append(node)
        while stack_2:
            print(stack_2.pop().data)
    # 队栈实现层次遍历
    def level_queueAndStack(self,root):
        if root==None:
            return
        stack_1=[]
        stack_2=[]
        stack_1.append(root)
        stack_2.append(root)
        while stack_1:
            node=stack_1.pop(0)
            if node.lchild:
                stack_1.append(node.lchild)
                stack_2.append(node.lchild)
            if node.rchild:
                stack_1.append(node.rchild)
                stack_2.append(node.rchild)
        while stack_2:
            print(stack_2.pop(0).data)


if __name__ == '__main__':
    list=[0,1,2,3,4,5,6,7,8,9,]
    tree=Tree()
    tree.createTree(list)
    tree.front_digui(tree.root)
    print('\n')
    tree.middle_digui(tree.root)
    print('\n')
    tree.behind_digui(tree.root)
    print('\n')
    tree.front_queueAndStack(tree.root)
    print('\n')
    tree.middle_queueAndStack(tree.root)
    print('\n')
    tree.behind_queueAndStack(tree.root)
    print('\n')
    tree.level_queueAndStack(tree.root)