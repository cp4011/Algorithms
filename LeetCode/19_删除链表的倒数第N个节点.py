"""给定一个链表，删除链表的倒数第 n 个节点，并且返回链表的头结点。
示例：
给定一个链表: 1->2->3->4->5, 和 n = 2.
当删除了倒数第二个节点后，链表变为 1->2->3->5.
说明：给定的 n 保证是有效的。
进阶：
你能尝试使用一趟扫描实现吗？
"""

'''一次遍历（双指针法、快慢指针）
        1. 添加虚拟头结点方便删除第一个节点
        2. 找到倒数第n个节点的前一个节点(也就是倒数n+1节点) 指向倒数第n个节点的下一个节点
        使用两个指针p,q, q先走n+1步,然后p,q一起走直到q走完整条链表,最后p指向的就是倒数n+1个节点
'''


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int):
        if not head:
            return
        first = ListNode(-1)        # 添加节点，防止头结点head被删掉了
        first.next = head

        p = first                   # p、q两指针保持 n+1 步的距离，这样才可删掉q指针下一个的节点（即导数第n个节点）
        q = head
        i = 0
        while i < n:                # q指针 移动n次
            q = q.next
            i += 1
        while q:                    # 最后 p指向的就是倒数n+1个节点
            q = q.next
            p = p.next
        p.next = p.next.next        # 将倒数第n个节点的前一个节点(倒数n+1节点) 指向倒数第n个节点的下一个节点
        return first.next
