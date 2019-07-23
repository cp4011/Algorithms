"""合并 k 个排序链表，返回合并后的排序链表。请分析和描述算法的复杂度。
示例:
输入:
[
  1->4->5,
  1->3->4,
  2->6
]
输出: 1->1->2->3->4->4->5->6
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    """优先级队列  时间复杂度：O(n*log(k))，n 是所有链表中元素的总和，k 是链表个数。"""
    def mergeKLists(self, lists):
        import heapq                    # 堆中的元素可以为元组，可对带权值的元素进行排序。
        first = ListNode(0)
        p = first
        heap1 = []                       # 构建小顶堆
        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(heap1, (lists[i].val, i))     # 将个链表中的头指针的 值和所在链表的顺序i 作为元组压入堆中
                lists[i] = lists[i].next                    # 各链表指向各自链表的第二个节点，一次是4 3 6
        # head堆中目前有 (1,1) (1,2) (2,2)
        while heap1:                     # 遍历小顶堆（弹出的栈顶元素，一定是当前值最小的和链表最靠前的）
            val, idx = heapq.heappop(heap1)  # 【错误】 head.pop() 注意是heapq.heappop(堆)
            p.next = ListNode(val)      # 改变指针指向
            p = p.next                  # 指针后移
            if lists[idx]:
                heapq.heappush(heap1, (lists[idx].val, idx))     # 将该链表当前以及遍历val的节点下一个节点的元组压入堆中
                lists[idx] = lists[idx].next                    # 该链表指针后移
        return first.next

    """分而治之 链表两两合并"""
    def mergeKLists1(self, lists):
        if not lists:
            return
        n = len(lists)
        return self.merge(lists, 0, n-1)

    def merge(self, lists, left, right):
        if left == right:
            return lists[left]
        mid = left + (right - left) // 2        # 地板除
        l1 = self.merge(lists, left, mid)
        l2 = self.merge(lists, mid+1, right)
        return self.mergeTwoLists(l1, l2)

    def mergeTwoLists(self, l1, l2):
        if not l1:return l2
        if not l2:return l1
        if l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2
