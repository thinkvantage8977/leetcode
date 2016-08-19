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

    def swapPairs(self, head):

        if not head:
            return None

        if not head.next:
            return head

        l1 = head
        l2 = head.next
        l1.next = l2.next
        l2.next = l1
        head = l2
        h = l1
        while h.next and h.next.next:
            l1 = h
            l2 = h.next
            l3 = h.next.next
            l1.next = l3
            l2.next = l3.next
            l3.next = l2
            h = l2

        return head


Head = ListNode(1)
#Head.next = ListNode(2)
#Head.next.next = ListNode(3)
#Head.next.next.next = ListNode(4)
#Head.next.next.next.next = ListNode(5)
#Head.next.next.next.next.next = ListNode(6)
#Head.next.next.next.next.next.next = ListNode(7)
#Head.next.next.next.next.next.next.next = ListNode(8)
#Head.next.next.next.next.next.next.next.next = Head.next.next.next.next.next


testClass = Solution()

print(printList(testClass.swapPairs(Head)))
