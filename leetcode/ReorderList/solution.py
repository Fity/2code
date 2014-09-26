# Definition for singly-linked list.
class ListNode:

    def __init__(self, x):
        self.val = x
        self.next = None

    def printList(self):
        head = self
        while head:
            print head,
            head = head.next
        print ''

    def __str__(self):
        return str(self.val)


class Solution:
    # @param head, a ListNode
    # @return nothing

    def reorderList(self, head):
        if head is None or head.next is None:
            return head
        slow = fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        prev = slow.next
        slow.next = None

        # reverse the second part of the list
        cur = prev.next
        prev.next = None
        while cur:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next

        # merge the two sublist
        root = head
        while prev:
            tmp = prev.next
            prev.next = root.next
            root.next = prev
            root = prev.next
            prev = tmp
        return head


def main():
    import random
    root = ListNode(random.randint(1, 1000))
    head = root
    for x in xrange(9):
        head.next = ListNode(random.randint(1, 1000))
        head = head.next
    root.printList()
    s = Solution()
    root = s.reorderList(root)
    root.printList()


if __name__ == '__main__':
    main()
