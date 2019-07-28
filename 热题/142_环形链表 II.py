"""给定一个链表，返回链表开始入环的第一个节点。 如果链表无环，则返回 null。
为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。 如果 pos 是 -1，则在该链表中没有环。
说明：不允许修改给定的链表。
示例 1：
输入：head = [3,2,0,-4], pos = 1
输出：tail connects to node index 1
解释：链表中有一个环，其尾部连接到第二个节点。
示例 2：
输入：head = [1,2], pos = 0
输出：tail connects to node index 0
解释：链表中有一个环，其尾部连接到第一个节点。
示例 3：
输入：head = [1], pos = -1
输出：no cycle
解释：链表中没有环。
进阶： 你是否可以不用额外空间解决此题？
"""


class Solution(object):
    def detectCycle(self, head):    # 快慢指针, 空间复杂度O(1)
        """快慢指针( 1. 先用快慢指针, 找到他们相遇点(如果存在环)
                    2. 再重新从链表头开始, 以及步骤1的相遇点, 两个位置一起走, 再次相遇就是环的入口)        """
        if not head or not head.next: return
        slow = head             # 快慢指针
        fast = head

        start = head            # 重新开始
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:    # 找到相遇点
                while slow != start:
                    slow = slow.next
                    start = start.next
                return slow
        return None

    def detectCycle1(self, head):    # 哈希, 空间复杂度O(n), 把遍历过的节点记录,当发现遍历的节点下一个节点遍历过, 返回它
        lookup = set()
        p = head
        while p:
            lookup.add(p)
            if p.next in lookup:
                return p.next
            p = p.next
        return None
