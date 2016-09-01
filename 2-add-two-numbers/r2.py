# Definition for singly-linked list.
class ListNode(object):

    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):

    def addTwoNumbers(self, l1, l2):
        h = nodeHead = ListNode(0)

        c = 0
        s = 0
        while l1 or l2:
            s = 0
            if l1:
                s += l1.val
                l1 = l1.next
            if l2:
                s += l2.val
                l2 = l2.next

            s += c
            c = s // 10
            s = s % 10
            h.next = ListNode(s)
            h = h.next
        if c != 0:
            h.next = ListNode(c)

        return nodeHead.next


# Setup testClass
testClass = Solution()

# Test input
l1 = ListNode(2)
head1 = l1

l1.next = ListNode(4)
l1 = l1.next

l1.next = ListNode(9)
l1 = l1.next


l2 = ListNode(1)
head2 = l2

l2.next = ListNode(6)
l2 = l2.next

l2.next = ListNode(3)
l2 = l2.next


# Run
result = testClass.addTwoNumbers(head1, head2)

# Print

while result.next != None:
    print(result.val, "->", end="")
    result = result.next

print(result.val)
