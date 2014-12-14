# -*- coding:utf-8 -*-
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    # @param a ListNode
    # @return a ListNode
    def swapPairs(self, head):
        if not head:
            return head
        if head.next is None:
            return head
        first = head
        second = head.next
        while second:
            first.val, second.val = second.val, first.val
            first = second.next
            if not first:
                break
            second = first.next
        return head
