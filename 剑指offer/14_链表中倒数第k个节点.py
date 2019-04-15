"""输入一个链表，输出该链表中倒数第k个结点。
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def FindKthToTail(self, head, k):
        if not head:
            return head
        node = head
        l = []
        while node:
            l.append(node)
            node = node.next
        if k > len(l) or k < 1:         # 【注意边界条件】 【or】
            return
        return l[-k]
