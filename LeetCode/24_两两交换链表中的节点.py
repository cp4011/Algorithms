"""给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。
示例: 给定 1->2->3->4, 你应该返回 2->1->4->3.
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# 迭代
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head: return
        first = ListNode(-1)
        p = first
        q = head
        if q and not q.next:        # 处理只有一个元素的情况，若无单独处理，[1]将得不到输出
            p.next = q
        while q and q.next:         # 后面不用考虑处理最后落单的元素，因为两两节点交换的时候会把后面指向的节点带上，只用考虑出事情可只有一个元素的情况
            temp = q.next
            p.next = temp           # 交换 位置
            q.next = temp.next
            temp.next = q

            q = q.next              # 指针后移
            p = p.next.next

        return first.next

    # 递归
    def swapPairs1(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        tmp = head.next
        head.next = self.swapPairs(head.next.next)
        tmp.next = head
        return tmp
