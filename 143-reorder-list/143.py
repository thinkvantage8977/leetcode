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

    def mergeTwoLists(self, l1, l2):
        dummy = ListNode(0)
        h = dummy

        while l1:
            h.next = l1
            l1 = l1.next
            h = h.next

            if l2:
                h.next = l2
                l2 = l2.next
                h = h.next

        return dummy.next

    def reverseList(self, head):
        reversedL2 = None
        while head:
            n = head
            head = head.next
            n.next = reversedL2
            reversedL2 = n
        return reversedL2

    def reorderList(self, head):
        if not head:
            return None

        fast = slow = head

        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next

        l2 = slow.next
        slow.next = None
        l1 = head

        rl2 = self.reverseList(l2)

        head = self.mergeTwoLists(l1,rl2)


Head1 = ListNode(1)
# Head1.next = ListNode(2)
# Head1.next.next = ListNode(3)
# Head1.next.next.next = ListNode(2)
# Head1.next.next.next.next = ListNode(2)

testClass = Solution()

printList(testClass.reorderList(Head1))
