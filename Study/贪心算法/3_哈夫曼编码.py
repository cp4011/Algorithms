"""哈夫曼编码可对指定的字符数据集进行数据压缩，压缩率在20%-90%。构造一种有效率的编码类型，使用该编码表达字符内容时可产生平均长度最短的位串"""


# Tree-Node Type
class Node:
    def __init__(self, freq):
        self.left = None
        self.right = None
        self.father = None
        self.freq = freq

    def isLeft(self):
        return self.father.left == self


# create nodes创建叶子节点
def createNodes(freqs):
    return [Node(freq) for freq in freqs]


import copy
# create Huffman-Tree创建Huffman树
def createHuffmanTree(nodes):
    queue = copy.copy(nodes)                    # 浅复制【复制列表中各子对象node的地址，指向各node节点】，queue = nodes[:]
    while len(queue) > 1:
        queue.sort(key=lambda item: item.freq)
        node_left = queue.pop(0)                # python中的赋值，都是内存地址的传递【赋值，浅拷贝，深拷贝只针对可变变量，如list，dict,tuple】
        node_right = queue.pop(0)

        node_father = Node(node_left.freq + node_right.freq)

        node_father.left = node_left
        node_father.right = node_right

        node_left.father = node_father
        node_right.father = node_father

        queue.append(node_father)
    queue[0].father = None
    return queue[0]


# Huffman编码
def huffmanEncoding(nodes, root):               # 从始至终，各node树节点都只有一份对象，只是它们的内存地址被保存了两份
    codes = [''] * len(nodes)
    for i in range(len(nodes)):
        node_tmp = nodes[i]
        while node_tmp != root:
            if node_tmp.isLeft():
                codes[i] = '0' + codes[i]
            else:
                codes[i] = '1' + codes[i]
            node_tmp = node_tmp.father
    return codes


if __name__ == '__main__':
    chars_freqs = [('C', 2), ('G', 2), ('E', 3), ('K', 3), ('B', 4),
                 ('F', 4), ('I', 4), ('J', 4), ('D', 5), ('H', 6),
                 ('N', 6), ('L', 7), ('M', 9), ('A', 10)]
    nodes = createNodes([item[1] for item in chars_freqs])
    root = createHuffmanTree(nodes)
    codes = huffmanEncoding(nodes, root)
    for item in zip(chars_freqs, codes):
        print('Character:%s freq:%-2d   encoding: %s' % (item[0][0], item[0][1], item[1]))


