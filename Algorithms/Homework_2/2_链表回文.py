'''链表回文
Description
判断一个单向链表是否为回文结构。自定义链表数据结构，要求时间复杂度为O(n)，额外空间复杂度为O(1)。
Input
输入的每一行的值用空格隔开，第一个值为节点个数，后面为每一个节点值
Output
是回文则输出true，不是则输出false，一行表示一个链表的结果。
Sample Input 1
3 1 2 1
4 1 2 2 1
3 3 5 3
6 a b c d c a
Sample Output 1
true
true
true
false
'''
#无链表
# while(True):
#     try:
#         list1 =input().split(' ')[1:]
#         list2=list1[::-1]
#         if list1==list2:
#             print('true')
#         else:
#             print('false')
#     except:
#         break


class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


def isHuiwen(node):
    head = node
    len = 0
    while head is not None:    #得到链表的长度len
        len += 1
        head = head.next

    head = node
    count = 0
    prehead = None            #前指针
    curhead = head            #当前指针
    posthead = curhead.next   #后指针
    while curhead is not None:
        if count == len//2:   #当count到了链表的一半，退出while
            break
        count += 1
        curhead.next = prehead #将前一半链表指针反转
        prehead = curhead
        curhead = posthead
        posthead = posthead.next

    if len % 2 == 0: #当链表长度为偶数时
        x = prehead
        y = curhead
    else:
        x = prehead
        y = posthead
    while x is not None and y is not None: #链表两侧是否相同
        if x.data != y.data:
            return False
        x = x.next
        y = y.next
    return True
try:
    while True:
        s = input().split(' ')
        array = []
        for item in s:
            array.append(item)
        num = int(array[0])
        array = array[1:num+1]

        linkedlist = Node(0, Node)
        head = linkedlist
        for item in array:
            linkedlist.next = Node(item, None)
            linkedlist = linkedlist.next

        if isHuiwen(head.next):
            print("true")
        else:
            print("false")
except EOFError:
    pass