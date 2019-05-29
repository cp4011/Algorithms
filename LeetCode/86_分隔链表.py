"""给定一个链表和一个特定值 x，对链表进行分隔，使得所有小于 x 的节点都在大于或等于 x 的节点之前。
你应当保留两个分区中每个节点的初始相对位置。
示例:
输入: head = 1->4->3->2->5->2, x = 3
输出: 1->2->2->4->3->5
"""
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def partition(self, head, x):
        h1 = l1 = ListNode(0)       # 定义工作指针l1和l2
        h2 = l2 = ListNode(0)       # 固定h1和h2指针在头部，利于返回
        while head:
            if head.val < x:
                l1.next = head
                l1 = l1.next        # 记得要 指针后移
            else:
                l2.next = head
                l2 = l2.next
            head = head.next
        l2.next = None              # 注意链表最后一个节点l2要指向空（可能没分割链表之前l2节点的next是指向其他节点的
        l1.next = h2.next           # 将小于x链表的最后一个节点l1的next指向h2头的第一个实节点
        return h1.next              # 返回头结点
