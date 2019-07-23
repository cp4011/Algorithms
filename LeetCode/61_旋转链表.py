"""给定一个链表，旋转链表，将链表每个节点向右移动 k 个位置，其中 k 是非负数。
示例 1:
输入: 1->2->3->4->5->NULL, k = 2
输出: 4->5->1->2->3->NULL
解释:
向右旋转 1 步: 5->1->2->3->4->NULL
向右旋转 2 步: 4->5->1->2->3->NULL
示例 2:
输入: 0->1->2->NULL, k = 4
输出: 2->0->1->NULL
解释:
向右旋转 1 步: 2->0->1->NULL
向右旋转 2 步: 1->2->0->NULL
向右旋转 3 步: 0->1->2->NULL
向右旋转 4 步: 2->0->1->NULL
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:             # 快慢双指针
    def rotateRight(self, head, k):    # 输入: 1->2->3->4->5->NULL, k = 2    输出: 4->5->1->2->3->NULL
        if not head or not head.next or k == 0:
            return head
        cur, length = head, 0
        while cur:
            length += 1
            cur = cur.next
        k %= length
        if k == 0:
            return head
        fast = slow = head
        for _ in range(k):          # fast指针 先走k个节点
            fast = fast.next
        while fast and fast.next:   # fast是最后一个节点的时候（节点5），low是倒数第k个节点（节点3）
            fast = fast.next
            slow = slow.next
        ret = slow.next             # ret为节点4
        fast.next = head
        slow.next = None
        return ret

