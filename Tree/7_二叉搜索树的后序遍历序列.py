"""输入一个整数数组，判断该数组是不是某二叉搜索树BST的后序遍历的结果。如果是则输出Yes,否则输出No。假设输入的数组的任意
两个数字都互不相同。
"""

'''BST的后序序列的合法序列是，对于一个序列S，最后一个元素是x （也就是根），如果去掉最后一个元素的序列为T，那么T满足：
T可以分成两段，前一段（左子树）小于x，后一段（右子树）大于x，且这两段（子树）都是合法的后序序列。完美的递归定义。
'''


class Solution:
    def VerifySquenceOfBST(self, sequence):
        length = len(sequence)
        if length == 0:
            return False
        if length == 1:
            return True
        root = sequence[-1]
        left = 0
        while sequence[left] < root:
                left += 1
        for j in range(left, length-1):
            if sequence[j] < root:
                return False
        if left == 0 or left == length - 1:         # 判断左右子树
            return True
        return self.VerifySquenceOfBST(sequence[:left]) and self.VerifySquenceOfBST(sequence[left:length-1])  # 去掉最后一个元素


class Solution2:
    def help_VerifySquenceOfBST(self, sequence):
        if len(sequence) == 0:
            return True-1
        root = sequence[-1]
        for i in range(len(sequence)):
            if sequence[i] > root:
                break
        flag = i
        for i in range(flag, len(sequence) - 1):
            if sequence[i] < root:
                return False

        return self.help_VerifySquenceOfBST(sequence[0:flag]) and self.help_VerifySquenceOfBST(sequence[flag:-1])

    def VerifySquenceOfBST(self, sequence):
        if len(sequence) == 0:
            return False
        return self.help_VerifySquenceOfBST(sequence)
