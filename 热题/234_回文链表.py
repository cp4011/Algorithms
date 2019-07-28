"""请判断一个链表是否为回文链表。
示例 1:   输入: 1->2
输出: false
示例 2:   输入: 1->2->2->1
输出: true
进阶：
你能否用 O(n) 时间复杂度和 O(1) 空间复杂度解决此题？
"""
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
'''f 记录快指针，每次走倆步，s 记录慢指针，每次走一步，p 记录 s 的前一个节点
首先使用快慢指针找到中点，第一个 while 停止时如果链表长度为奇数，f不为空，s为中点，s 前进一步；
否则 f 为 None，s 为右半部分的第一个节点（直接开始比对，s不需前移一步），然后 p 和 s 往俩个方向同时遍历比对是否回文'''
class Solution:
    def isPalindrome(self, head):
        s, f, p = head, head, None
        while f and f.next:     # f 记录快指针，每次走倆步，s 记录慢指针，每次走一步，p 记录 s 的前一个节点
            s.next, p, s, f = p, s, s.next, f.next.next
        if f:                   # f不为空，说明链表长度为奇数，s此时正在中点
            s = s.next          # s前移一步
        while s and p and s.val == p.val:   # p 和 s 往俩个方向同时遍历比对是否回文
            p, s = p.next, s.next
        return s == p == None
