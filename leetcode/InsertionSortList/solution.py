import random

# Definition for singly-linked list.


class ListNode:

    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # @param head, a ListNode
    # @return a ListNode

    def insertionSortList(self, head):
        if head is None:
            return head
        cur = head
        root = ListNode(0)
        root.next = head
        while cur.next is not None:
            if cur.val > cur.next.val:
                prev = root
                while prev.next.val < cur.next.val:
                    prev = prev.next
                tmp = cur.next
                cur.next = cur.next.next
                tmp.next = prev.next
                prev.next = tmp
            else:
                cur = cur.next
        head = root.next
        root = None
        return head

    def printList(self, head):
        cur = head
        while cur:
            print cur.val, '->',
            cur = cur.next
        print ''


if __name__ == '__main__':
    head = None
    for x in xrange(10):
        if head == None:
            head = ListNode(random.randint(1, 10000))
            cur = head
        else:
            cur.next = ListNode(random.randint(1, 10000))
            cur = cur.next
    s = Solution()
    print 'before'
    s.printList(head)
    head = s.insertionSortList(head)
    print 'after'
    s.printList(head)
