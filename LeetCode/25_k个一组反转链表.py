"""给出一个链表，每 k 个节点一组进行翻转，并返回翻转后的链表。
k 是一个正整数，它的值小于或等于链表的长度。如果节点总数不是 k 的整数倍，那么将最后剩余节点保持原有顺序。
示例 :
给定这个链表：1->2->3->4->5
当 k = 2 时，应当返回: 2->1->4->3->5
当 k = 3 时，应当返回: 3->2->1->4->5
说明 :
你的算法只能使用常数的额外空间。
你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        """用栈，我们把 k 个数压入栈中，然后弹出来的顺序就是翻转的！
        需注意：  1.剩下的链表个数够不够 k 个 不用翻转；  2.已经翻转的部分要与剩下链表连接起来"""
        if not head: return
        first = ListNode(-1)    # 新建指针
        p = first               # 已经反转节点的最后一个节点的指针
        q = head                # q指针 还没反转的第一个节点指针，记录链表第1, k+1, 2k+1的节点位置【防止剩余链表长度不够k个节点，p指针可以指向剩余的链表头结点指针q】
        tail = head             # 工作指针
        while True:
            stack = []
            count = k
            while count and tail:          # count为0 或 tail为None 时 结束将节点压栈
                stack.append(tail)
                tail = tail.next
                count -= 1
            if count:                      # count不为0，则此时的tail为空，所以剩下的链表节点不够k个了
                p.next = q                 # 已经反转了的最后一个指针p 指向还未反转的第一个节点指针q，结束循环
                break
            while stack:
                p.next = stack.pop()       # 翻转
                p = p.next
            p.next = tail                  # 与剩下链表连接起来，指针q指向tail
            q = tail                       # 更新指针q【后移k个
        return first.next

    # 递归
    def reverseKGroup1(self, head: ListNode, k: int) -> ListNode:
        cur = head
        count = 0
        while cur and count != k:
            cur = cur.next
            count += 1
        if count == k:
            cur = self.reverseKGroup(cur, k)
            while count:
                tmp = head.next
                head.next = cur
                cur = head
                head = tmp
                count -= 1
            head = cur
        return head

