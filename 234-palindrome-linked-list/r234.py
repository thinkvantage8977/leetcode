# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):

    def isPalindrome(self, head):
        if not head:
            return True

        fast = slow = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        stack = [slow.val]

        while slow.next:
            stack.append(slow.next.val)
            slow = slow.next

        fast = head

        while stack:
            if stack.pop() != fast.val:
                return False
            fast = fast.next
        return True
