"""给定一个排序链表，删除所有含有重复数字的节点，只保留原始链表中 没有重复出现 的数字。
示例 1:
输入: 1->2->3->3->4->4->5
输出: 1->2->5
示例 2:
输入: 1->1->1->2->3
输出: 2->3
"""



class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        first = ListNode(-1)
        first.next = head   # 定义一个first指向头结点，防止head被删除掉
        p, q = first, head
        while q:            # 【特别注意循环和判断的 条件设置】
            if q.next and q.val == q.next.val:      # 若有元素重复
                while q.next and q.val == q.next.val:  # if判断中加一个while循环是为了让q指针遍历到重复元素的最后一个节点
                    q = q.next
                q = q.next      # q指针右移1位，并将指针p的下一个节点指向q，即将中间的全部重复节点删掉
                p.next = q
            else:                                   # 若无元素重复，p、q两指针右移1位
                p = p.next
                q = q.next
        return first.next


