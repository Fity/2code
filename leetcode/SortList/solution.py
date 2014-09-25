# Definition for singly-linked list.
# class ListNode:

#    def __init__(self, x):
#        self.val = x
#        self.next = None


class Solution:
    # @param head, a ListNode
    # @return a ListNode

    def sortList(self, head):
        '''merge sort from bottom up
        '''
        if head is None or head.next is None:
            # empty list or there is only one node.
            return head
        fast = head
        slow = head
        while fast.next is not None and fast.next.next is not None:
            slow = slow.next
            fast = fast.next.next
        l1 = head
        l2 = slow.next
        slow.next = None

        l1 = self.sortList(l1)
        l2 = self.sortList(l2)
        head = self.merge(l1, l2)

        return head

    def merge(self, l1, l2):
        head = None
        if l1.val > l2.val:
            head = l2
            l2 = l2.next
        else:
            head = l1
            l1 = l1.next
        cur = head
        while l1 is not None and l2 is not None:
            if l1.val > l2.val:
                cur.next = l2
                l2 = l2.next
            else:
                cur.next = l1
                l1 = l1.next
            cur = cur.next
        if l1:
            cur.next = l1
        if l2:
            cur.next = l2
        return head
