# Definition for singly-linked list.
class ListNode(object):

    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):

    def reverseKGroup(self, head, k):

        dummy = ListNode(-1)
        if not head or k == 1:
            return head

        dummy.next = head

        pre = dummy
        reverse = None
        current = dummy.next

        while current:

            i = 0
            while i < k - 1:
                n = current.next
                current.next = reverse
                reverse = current
                current = n

            pre.next.next = 
