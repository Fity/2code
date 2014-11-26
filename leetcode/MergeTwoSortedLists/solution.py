# -*- coding:utf-8 -*-
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    # @param two ListNodes
    # @return a ListNode

    def mergeTwoLists(self, l1, l2):
        if not l1:
            return l2
        if not l2:
            return l1

        head = None
        if l1.val > l2.val:
            head = l2
            l2 = l2.next
        else:
            head = l1
            l1 = l1.next
        index = head
        while l1 and l2:
            if l1.val > l2.val:
                index.next = l2
                l2 = l2.next
            else:
                index.next = l1
                l1 = l1.next
            index = index.next
        if l1:
            index.next = l1
        elif l2:
            index.next = l2
        return head
