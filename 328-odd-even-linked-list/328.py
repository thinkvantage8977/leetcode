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
        oddHead = head

        if not head.next:
            return head
        evenHead = head.next
        odd = oddHead
        even = evenHead

        p = head.next.next
        i = 0

        while p:
            if i == 0:
                odd.next = p
                p = p.next
                odd = odd.next
            else:
                even.next = p
                p = p.next
                even = even.next

            i = (i + 1) % 2

        even.next = None
        odd.next = evenHead

        return oddHead


Head = ListNode(1)
Head.next = ListNode(2)
Head.next.next = ListNode(3)
# Head.next.next.next = ListNode(4)
# Head.next.next.next.next = ListNode(5)
# Head.next.next.next.next.next = ListNode(6)
# Head.next.next.next.next.next.next = ListNode(7)



testClass = Solution()

print(printList(testClass.oddEvenList(Head)))
