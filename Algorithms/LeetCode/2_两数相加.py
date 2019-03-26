"""给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。
如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。
您可以假设除了数字 0 之外，这两个数都不会以 0 开头。
示例：
输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
输出：7 -> 0 -> 8
原因：342 + 465 = 807
"""


class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None


def create_nodes(arr):
    return [ListNode(i) for i in arr]


def create_listnodes(nodes):
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]
    nodes[-1].next = None
    return nodes[0]


class Solution:
    def addTwoNumbers(self, l1, l2):
        root = node = ListNode(0)
        carry = 0
        while l1 or l2 or carry:
            value1 = value2 = 0
            if l1:
                value1 = l1.value
                l1 = l1.next
            if l2:
                value2 = l2.value
                l2 = l2.next
            carry, mod = divmod(value1 + value2 + carry, 10)
            node.next = ListNode(mod)
            node = node.next
        return root.next


nodes1 = create_nodes([2, 4, 3])
nodes2 = create_nodes([5, 6, 4])
listnodes1 = create_listnodes(nodes1)
listnodes2 = create_listnodes(nodes2)
root = Solution().addTwoNumbers(listnodes1, listnodes2)
while root:
    print(root.value)
    root = root.next
