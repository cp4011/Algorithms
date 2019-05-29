"""反转从位置 m 到 n 的链表。请使用一趟扫描完成反转。说明: 1 ≤ m ≤ n ≤ 链表长度。
示例:     输入: 1->2->3->4->5->NULL, m = 2, n = 4       输出: 1->4->3->2->5->NULL
"""
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseBetween(self, head, m, n):
        dummy = pre = ListNode(0)
        dummy.next = head
        for _ in range(m - 1):      # pre指针移动m-1个节点，最终指向 节点1（要开始反转的链表节点的前一个节点）
            pre = pre.next
        cur = pre.next              # cur节点 指向要开始反转的链表节点2
        # 开始反转链表
        node = None
        for _ in range(n - m + 1):  # 要反转 n-m+1次，最后node是反转链表最后一个节点4，而cur则是节点5
            nxt = cur.next
            cur.next = node
            node = cur
            cur = nxt
        # 连接三个部分
        pre.next.next = cur         # 节点1 pre.next一直指向的都是 节点2，将节点2指向cur（节点5）
        pre.next = node             # 将节点1 指向 node（节点4）
        return dummy.next

