"""在 O(nlogn) 时间复杂度和常数级空间复杂度下，对链表进行排序。
示例 1:
输入: 4->2->1->3
输出: 1->2->3->4
示例 2:
输入: -1->5->3->4->0
输出: -1->0->3->4->5
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:         # 归并（在 O(nlogn) 时间复杂度和常数级空间复杂度下，对链表进行排序。）
    def sortList(self, head: ListNode) -> ListNode:
        if not head or not head.next: return head   # 结束（递归切分结束）.
        # 切分
        slow, fast = head, head.next
        while fast and fast.next:                   # 链表对半切分
            fast, slow = fast.next.next, slow.next
        mid, slow.next = slow.next, None            # 切分，并将前半段的尾部slow指向空none
        left, right = self.sortList(head), self.sortList(mid)   # 递归切分
        # 合并
        h = res = ListNode(0)                       # 定义头指针
        while left and right:                       # 合并左 右链表并返回
            if left.val < right.val: h.next, left = left, left.next
            else: h.next, right = right, right.next
            h = h.next
        h.next = left if left else right            # 左右其中一个为空，另一个还有节点时
        return res.next

    def sortList1(self, head: ListNode) -> ListNode:
        if not (head and head.next): return head
        pre, slow, fast = None, head, head
        while fast and fast.next: pre, slow, fast = slow, slow.next, fast.next.next
        pre.next = None         # pre是前半部分节点的尾节点，slow是后半部分的头结点，fast整个链表的尾节点
        return self.mergeTwoLists(*map(self.sortList, (head, slow)))

    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 and l2:
            if l1.val > l2.val: l1, l2 = l2, l1
            l1.next = self.mergeTwoLists(l1.next, l2)
        return l1 or l2     # 0 or 2 : 2     2 and 3 : 3
