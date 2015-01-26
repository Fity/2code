# -*- coding:utf-8 -*-
tion for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @param k, an integer
    # @return a ListNode
    def rotateRight(self, head, k):
        if head is None or head.next is None:
            return head

        index = head
        lens = 0
        count = 0
        while index is not None:
            index = index.next
            count += 1
        k = k % count
        if k == 0:
            return head

        slow = head
        fast = head.next
        prev = head
        while k > 0:
            prev = fast
            fast = fast.next
            k -= 1
        while fast is not None:
            prev = fast
            fast = fast.next
            slow = slow.next

        new_head = slow.next
        slow.next = None
        prev.next = head
        return new_head

