"""序列化是将一个数据结构或者对象转换为连续的比特位的操作，进而可以将转换后的数据存储在一个文件或者内存中，同时也可以通过
网络传输到另一个计算机环境，采取相反方式重构得到原数据。
请设计一个算法来实现二叉树的序列化与反序列化。这里不限定你的序列 / 反序列化算法执行逻辑，你只需要保证一个二叉树可以被序列化
为一个字符串并且将这个字符串反序列化为原始的树结构。
示例:     你可以将以下二叉树：
    1
   / \
  2   3
     / \
    4   5
序列化为 "[1,2,3,null,null,4,5]"
说明: 不要使用类的成员 / 全局 / 静态变量来存储状态，你的序列化和反序列化算法应该是无状态的。
"""
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:                        # 前序遍历 DFS
    def serialize(self, root):      # 只访问每个节点一次，因此时间复杂度为 O(n)O(n)，其中 nn 是节点数
        def rserialize(root, string):
            if root is None:
                string += 'None,'   # 此处不能 return None【所以要用if else】,不然会导致else中 string会为空None
            else:
                string += str(root.val) + ','
                string = rserialize(root.left, string)  # 若上面有return None，则会有string为空，导致string += 'None,'报错，空类型 + 字符串类型
                string = rserialize(root.right, string)
            return string

        return rserialize(root, '')

    def deserialize(self, data):
        def rdeserialize(l):
            if l[0] == 'None':
                l.pop(0)
                return None
            root = TreeNode(l[0])
            l.pop(0)
            root.left = rdeserialize(l)
            root.right = rdeserialize(l)
            return root

        data_list = data.split(',')
        root = rdeserialize(data_list)
        return root


class Codec_wrong:      # 自己错误
    def serialize(self, root):
        def func_serialize(root, string):
            if not root:
                string += ",None"
                return None
            string += "root.val"
            func_serialize(root.left, string)
            func_serialize(root.right, string)
            return string

        return func_serialize(root, "")

    def deserialize(self, data):
        def func_deserialize(l):
            if not l:
                return None
            root = TreeNode(l.pop(0))
            root.left = func_deserialize(l)
            root.right = func_deserialize(l)
            return root

        l = data.split(",")
        return func_deserialize(l)