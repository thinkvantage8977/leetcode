# Definition for singly-linked list.
class ListNode(object):

    def __init__(self, x):
        self.val = x
        self.next = None


def printList(l):
    while l != None:
        print(l.val, end="")
        if l.next:
            print('->', end="")
        l = l.next
    print()


class Solution(object):

    def partition(self, head, x):
        if not head:
            return None

        smallerhead = smaller = ListNode(-1)
        largerhead = larger = ListNode(-1)

        h = head

        while h:
            if h.val < x:
                smaller.next = h
                smaller = smaller.next
            else:
                larger.next = h
                larger = larger.next
            h = h.next

        larger.next=None
        smaller.next = largerhead.next

        return smallerhead.next


Head = ListNode(19)
Head.next = ListNode(1)
Head.next.next = ListNode(22)
Head.next.next.next = ListNode(4)
Head.next.next.next.next = ListNode(51)
Head.next.next.next.next.next = ListNode(25)
Head.next.next.next.next.next.next = ListNode(7)
Head.next.next.next.next.next.next.next = ListNode(18)


testClass = Solution()

print(printList(testClass.partition(Head, 0)))
