"""给定一个排序链表，删除所有重复的元素，使得每个元素只出现一次。
示例 1:
输入: 1->1->2
输出: 1->2
示例 2:
输入: 1->1->2->3->3
输出: 1->2->3
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteDuplicates(self, head):
        cur = head
        while cur:                          # 1->1->1->2
            while cur.next and cur.next.val == cur.val:     # 第一轮，删除了第2个位置上的“1”；
                cur.next = cur.next.next                    # 第二轮还是满足条件，删除第3个位置上的“1”
            cur = cur.next   # 前面的循环，只是一直在改变cur指向的下一个节点，就是删除之后与cur重复的所有节点，循环结束后cur再右移
        return head                                         # 输出: 1->2

    def deleteDuplicates1(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        p = head
        while p:
            if p.next and p.val == p.next.val:
                temp = p
                while temp.next and temp.val == temp.next.val:
                    temp = temp.next
                p.next = temp.next
                p = temp.next
            else:
                p = p.next
        return head


l = [1, 1, 1, 2]
nodes = [ListNode(i) for i in l]
nodes[0].next = nodes[1]
nodes[1].next = nodes[2]
nodes[2].next = nodes[3]
Solution().deleteDuplicates1(nodes[0])
