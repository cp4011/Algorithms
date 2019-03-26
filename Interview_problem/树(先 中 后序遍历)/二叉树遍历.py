class Node:
    def __init__(self, root="NIL", left=None, right=None):
        self.root = root
        self.left = left
        self.right = right
        self.out_list_temp = []


class Tree(Node):
    def build(self, node_list):
        root = node_list.pop(0)
        if root == "NIL":
            tree = None
        else:
            tree = Tree(root)
            tree.left = self.build(node_list)
            tree.right = self.build(node_list)
        return tree

    def preorder_traversal(self, tree):
        if (tree.root != None):
            self.out_list_temp.append(tree.root)
        if tree.left != None:
            self.preorder_traversal(tree.left)
        if tree.right != None:
            self.preorder_traversal(tree.right)
        return self.out_list_temp

    def preorder_traversal_print(self, tree):
        print(self.preorder_traversal(tree))
        self.out_list_temp = []

    def inorder_traversal(self, tree):
        if tree.left != None:
            self.inorder_traversal(tree.left)
        if (tree.root != None):
            self.out_list_temp.append(tree.root)
        if tree.right != None:
            self.inorder_traversal(tree.right)
        return self.out_list_temp

    def inorder_traversal_print(self, tree):
        print(self.inorder_traversal(tree))
        self.out_list_temp = []

    def postorder_traversal(self, tree):
        if tree.left != None:
            self.postorder_traversal(tree.left)
        if tree.right != None:
            self.postorder_traversal(tree.right)
        if (tree.root != None):
            self.out_list_temp.append(tree.root)
        return self.out_list_temp

    def postorder_traversal_print(self, tree):
        print(self.postorder_traversal(tree))
        self.out_list_temp = []


if __name__ == '__main__':
    node_list = [1, 2, 4, 'NIL', 'NIL', 5, 'NIL', 'NIL', 3, 'NIL', 6, 7, 'NIL', 'NIL', 'NIL']
    tree = Tree()
    my_tree = tree.build(node_list)
    tree.preorder_traversal_print(my_tree)
    tree.inorder_traversal_print(my_tree)
    tree.postorder_traversal_print(my_tree)
