"""在一个排序的链表中，存在重复的结点，请删除该链表中重复的结点，重复的结点不保留，返回链表头指针。
例如，链表1->2->3->3->4->4->5 处理后为 1->2->5
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


'''注意区分 cur.next = temp 【这是改变此时工作指针cur指向的这个数据节点的next所指向的节点为temp节点】
而 cur = temp 【这是将工作指针cur所指向的节点往后移动】  
即 前者是改变该链表内数据节点的指向，后者cur只是个指针变量，指向链表数据节点的指针，不是一个节点，是工作指针
'''

class Solution:
    def deleteDuplication(self, pHead):
        if pHead is None or pHead.next is None:
            return pHead

        first_node = ListNode(-1)                        # 新建一个节点，防止头结点要被删除
        first_node.next = pHead

        pre = first_node    # 设置 pre ，cur 指针， pre指针指向当前确定不重复的那个节点，而cur指针相当于工作指针，一直往后面搜索。
        cur = pHead         # 如果改变cur的指向，相当于pHead也改变了，他们两共拥有一份内存对象  【d.next = cur】

        while cur:
            if cur.next and cur.next.val == cur.val:    # 如果当前节点的值和下一个节点的值相等
                temp = cur.next
                while temp and temp.val == cur.val:     # 向后重复查找，【改为temp.next，则保留一个重复中的元素，如3,4】
                    temp = temp.next
                pre.next = temp                         # 【指针赋值】该node节点的指向改变，就相当于删除中间的部分
                cur = temp                              # cur移到temp的节点上

            else:                                       # 如果当前节点和下一个节点值不等，则向后移动一位【并没有改变链表内部数据连接的指向关系】
                pre = cur
                cur = cur.next                          # 工作指针cur后移， 并没有改变内部数据链表的指向关系

        return first_node.next                          # 返回头结点的下一个节点


class Solution2:
    def deleteDuplication(self, pHead):
        if pHead is None or pHead.next is None:
            return pHead
        head1 = pHead.next
        if head1.val != pHead.val:
            pHead.next = self.deleteDuplication(pHead.next)
        else:
            while pHead.val == head1.val and head1.next is not None:
                head1 = head1.next
            if head1.val != pHead.val:
                pHead = self.deleteDuplication(head1)
            else:
                return None
        return pHead
