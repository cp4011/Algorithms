"""输入一个链表，反转链表后，输出新链表的表头。
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        if not pHead or not pHead.next:
            return pHead
        node = pHead
        last = None
        while node:                 # node为空的时候弹出，此时last就是最后一个元素
            tmp = node.next
            node.next = last
            last = node
            node = tmp
        return last
