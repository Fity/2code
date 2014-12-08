# -*- coding:utf-8 -*-
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def deleteDuplicates(self, head):
        if not head:
            return head
        prev = head
        root = head.next
        while root is not None:
            if prev.val == root.val:
                # remove duplicates
                prev.next = root.next
                root.next = None
                root = prev.next
            else:
                prev = root
                root = root.next
        return head
