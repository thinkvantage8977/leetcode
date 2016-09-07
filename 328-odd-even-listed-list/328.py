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

    def oddEvenList(self, head):
        if not head:
            return None

        oddh = head
        evenh = head.next

        odd = oddh
        even = evenh

        while even and odd and even.next and odd.next:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next

        even.next = None
        odd.next = evenh

        return oddh



Head = ListNode(1)
Head.next = ListNode(2)
Head.next.next = ListNode(3)
Head.next.next.next = ListNode(4)
Head.next.next.next.next = ListNode(5)
Head.next.next.next.next.next = ListNode(6)
Head.next.next.next.next.next.next = ListNode(7)



testClass =Solution()

result = testClass.oddEvenList(Head)

printList(result)