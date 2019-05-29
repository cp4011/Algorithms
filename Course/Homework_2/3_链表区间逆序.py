'''链表区间逆序
Description
将单个链表的每K个节点之间逆序，打印出新链表；最后不足K的节点数不需要逆序；要求时间复杂度为O(n)，额外空间复杂度为O(1)。
Input
输入的每一行的值用空格隔开，第一个表示链表长度，中间为节点值，最后代表K。
Output
输出的每一行为新的链表，节点值用空格隔开，末尾不要空格。
Sample Input 1
8 1 2 3 4 5 6 7 8 3
8 a b c d e f g h 4
Sample Output 1
3 2 1 6 5 4 7 8
d c b a h g f e
'''


#非链表实现法
# while True:
#     try:
#         list1 = input().split(' ')
#         length = int(list1[0])
#         k = int(list1[-1])
#         list2 = list1[1:-1]
#         splited_list = [list2[i:i + k] for i in range(0, len(list2), k) if (i+k <= length)]
#         reversed_list = [item[::-1] for item in splited_list]
#
#         result_str = ''
#         for i in reversed_list:
#             for j in i:
#                 result_str += str(j) + ' '
#         i = 0
#         while i+k <= length:
#             i += k
#         for j in list2[i:]:
#             result_str += str(j) + ' '
#         print(result_str[:-1])
#     except:
#         break


class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


def mysort(node, k):
    curnode = node
    size = 0
    while curnode is not None:
        size += 1
        curnode = curnode.next
    prenode = None              #用来逆序的三个指针
    curnode = node
    postnode = curnode.next
    count = 0
    while size >= k:
        curnode.next = prenode  #第一个指针反向指着空prenode
        prenode = curnode
        if postnode is not None:
            curnode = postnode
            postnode = postnode.next   #最后一次的时候postnode可以指向空None
        else:
            curnode = None
            postnode = None

        count += 1
        if count == k:
            tmp = prenode
            tmp_count = 0
            while tmp is not None:
                if curnode is None and tmp_count == k - 1:
                    print(tmp.data)
                else:
                    print(tmp.data, end=' ')
                tmp = tmp.next
                tmp_count += 1
                if tmp_count == k:
                    break
            count = 0
            size -= k
    tmp = curnode    #剩余最后的不足k个
    while tmp is not None:
        if tmp.next is not None:
            print(tmp.data, end=' ')
        else:
            print(tmp.data)
        tmp = tmp.next

try:
    while True:
        s = input().split(' ')
        array = []
        for item in s:
            array.append(item)
        num = int(array[0])
        k = int(array[num + 1])
        array = array[1:num+1]
        linkedlist = Node(0, Node)
        head = linkedlist
        for item in array:
            linkedlist.next = Node(item, None)
            linkedlist = linkedlist.next

        mysort(head.next, k)
except EOFError:
    pass