"""给定一个链表，判断链表中是否有环。
为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。 如果 pos 是 -1，则在该链表中没有环。
示例 1：
输入：head = [3,2,0,-4], pos = 1
输出：true
解释：链表中有一个环，其尾部连接到第二个节点。
示例 2：
输入：head = [1,2], pos = 0
输出：true
解释：链表中有一个环，其尾部连接到第一个节点。
示例 3：
输入：head = [1], pos = -1
输出：false
解释：链表中没有环。
"""


class Solution(object):     # 给定一个链表，判断链表中是否有环。
    def hasCycle(self, head):     # 快慢指针, 空间复杂度O(1),好像两个人在一个操场上跑步,速度快的人一定会和速度慢的相遇(环)
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

    def hasCycle1(self, head):     # 哈希, 空间复杂度O(n),把遍历过的节点记录,当发现遍历的节点下一个节点遍历过, 说明有环
        lookup = set()
        p = head
        while p:
            lookup.add(p)
            if p.next in lookup:
                return True
            p = p.next
        return False

