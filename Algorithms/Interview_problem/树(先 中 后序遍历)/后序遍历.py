# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root == None:
            return []
        stack, node = [root], root
        resLs = []
        while stack.__len__() > 0:
            node = stack.pop()
            resLs.append(node.val)
            if node.left != None:
                stack.append(node.left)
            if node.right != None:
                stack.append(node.right)

'''输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历的结果。如果是则输出Yes,否则输出No。
假设输入的数组的任意两个数字都互不相同。（基本思想：二叉搜索树满足左子节点值都小于根节点值，右子节点值都大于根节点值；
后序遍历的最后一个元素是根节点，序列中小于根节点的所有数构成左子树，大于根节点的所有数构成右子树）
'''
class Solution:
    def VerifySquenceOfBST(self, sequence):
        # write code here
        if len(sequence)==0:
            return False
        index = 0
        for index in xrange(len(sequence)-1):  ###找出左子树
            if sequence[index]>sequence[-1]:
                break
        for i in xrange(index+1,len(sequence)-1):  ###判断右子树的数是否比根节点大
            if sequence[i]<sequence[-1]:
                return False
        if self.check(sequence,0,index) and self.check(sequence,index+1,len(sequence)-1):
            return True
        else:
            return False
    def check(self,sequence,start,end):
        if start>=end:
            return True
        index = 0
        for index in xrange(start,end):
            if sequence[index]>sequence[end]:
                break
        for i in xrange(index+1,end):
            if sequence[i]<sequence[end]:
                return False
        return self.check(sequence,start,index) and self.check(sequence,index+1,end-1)
