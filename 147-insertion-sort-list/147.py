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

    def insertionSortList(self, head):
        if not head or not head.next:
            return head
        dummy = ListNode(-1)
        # dummy.next = head
        h = head

        while h:
            start = dummy

            while start.next and (start.next.val <= h.val):
                start = start.next

            temp = h.next

            h.next = start.next

            start.next = h

            h = temp

        return dummy.next



Head = ListNode(19)
Head.next = ListNode(1)
Head.next.next = ListNode(22)
Head.next.next.next = ListNode(4)
Head.next.next.next.next = ListNode(51)
Head.next.next.next.next.next = ListNode(25)
Head.next.next.next.next.next.next = ListNode(7)
Head.next.next.next.next.next.next.next = ListNode(18)


testClass = Solution()

print(printList(testClass.insertionSortList(Head)))
