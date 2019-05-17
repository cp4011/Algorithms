"""请实现两个函数，分别用来序列化和反序列化二叉树(用什么方法无所谓，关键是输入一棵树，序列化为字符串，然后将字符串反序列化
还能还原为原来的那棵树。)"""

'''     1. 对于序列化：使用前序遍历，递归的将二叉树的值转化为字符，并且在每次二叉树的结点不为空时，在转化val所得的字符
之后添加一个' ， '作为分割。对于空节点则以 '#' 代替。
        2. 对于反序列化：按照前序顺序，递归的使用字符串中的字符创建一个二叉树
 '''


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def Serialize(self, root):
        if not root:
            return '#,'             # 注意#后面 还有个【逗号，】
        return str(root.val) + ',' + self.Serialize(root.left) + self.Serialize(root.right)    # 注意left和right中间没有 + ','了

    def Deserialize(self, s):

        def help(l):
            if l[0] == '#':
                return
            root = TreeNode(int(l[0]))
            if l.pop(0):            # 先序遍历【根左右】，先构建左子树，依次弹出，反序列化该节点后就删掉
                root.left = help(l)
            if l.pop(0):
                root.right = help(l)
            return root

        l = s.split(',')
        return help(l)

    def __init__(self):             # 反序列化的第二种方法 定义Flag变量【相当于全局变量】，用于记录已经反序列化的位置
        self.flag = -1

    def Deserialize2(self, s):
        self.flag += 1
        if self.flag >= len(s):     # 已经反序列化完了所以元素
            return None
        root = None
        l = s.split(',')
        if l[self.flag] != '#':
            root = TreeNode(int(l[self.flag]))
            root.left = self.Deserialize(s)
            root.right = self.Deserialize(s)
        return root




