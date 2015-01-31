# -*- coding:utf-8 -*-
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    # @return a ListNode
    def addTwoNumbers(self, l1, l2):
        overflow = 0
        head = ListNode(0)
        node = head
        while l1 is not None or l2 is not None:
            node.next = ListNode(0)
            if l1 is None:
                v1 = 0
            else:
                v1 = l1.val
                l1 = l1.next
            if l2 is None:
                v2 = 0
            else:
                v2 = l2.val
                l2 = l2.next
            s = v1 + v2 + overflow
            node.next.val = s % 10
            overflow = s // 10
            node = node.next
        if overflow:
            node.next = ListNode(overflow)
        return head.next
