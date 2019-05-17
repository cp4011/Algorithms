"""给一个链表，若其中包含环，请找出该链表的环的入口结点，否则，输出null。"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def EntryNodeOfLoop(self, pHead):
        cur = pHead
        l = []
        while cur:                  # 遍历链表，环的存在，遍历遇见的第一个重复的即为入口节点
            if cur in l:
                return cur
            else:
                l.append(cur)
            cur = cur.next
        return None


"""         时间复杂度：O(n)       空间复杂度：O(1)
    1. 找环中相汇点。  分别用p1，p2指向链表头部，p1每次走一步，p2每次走二步，直到p1==p2找到在环中的相汇点。
    2. 找环的入口。   当p1==p2时，再让p2指向链表头部，p1位置不变，p1,p2每次走一步 ，直到p1==p2相遇; 此时p1相遇地点就是环的入口。
"""