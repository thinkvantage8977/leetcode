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

    def rotateRight(self, head, k):

        if not head:
            return head

        length = 1
        p = head

        while p.next:
            length += 1
            p = p.next

        k = k % length
        if k ==0:
        	return head

        curEnd = p

        p = head

        for i in range(length - k - 1):
            p = p.next

        newHead = p.next
        p.next = None
        curEnd.next = head

        return newHead


Head = ListNode(1)
Head.next = ListNode(2)
# Head.next.next = ListNode(3)
# Head.next.next.next = ListNode(4)
# Head.next.next.next.next = ListNode(5)

testClass = Solution()

print(printList(testClass.rotateRight(Head, 12)))
