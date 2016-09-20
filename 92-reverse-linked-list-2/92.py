# Definition for singly-linked list.
class ListNode(object):

    def __init__(self, x):
        self.val = x
        self.next = None


def printList(l):
    while l.next != None:
        print(l.val, end="")
        print('->', end="")
        l = l.next
    print(l.val)


class Solution(object):

    def reverseBetween(self, head, m, n):
        if m == n:
            return head

        dummy = ListNode(0)
        dummy.next = head

        pre = dummy

        for i in range(m - 1):
            pre = pre.next

        reverse = None
        current = pre.next

        for i in range(n - m + 1):
            n = current.next
            current.next = reverse
            reverse = current
            current = n

        pre.next.next = current
        pre.next = reverse

        return dummy.next


testClass = Solution()

Head = ListNode("5")
Head.next = ListNode("4")
Head.next.next = ListNode("3")
Head.next.next.next = ListNode("2")
Head.next.next.next.next = ListNode("1")


testClass.reverseBetween(Head, 2, 4)

printList(Head)
