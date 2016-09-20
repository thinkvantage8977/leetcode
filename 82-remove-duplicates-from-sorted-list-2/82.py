# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):

    def deleteDuplicates(self, head):
        if not head:
            return None
        d = {}
        h = head

        while h:
            if h.val in d:
                d[h.val] += 1
            else:
                d[h.val] = 1
            h = h.next
        dummy = ListNode(-1)
        dummy.next = head

        h = dummy

        while h.next:
            if d[h.next.val] > 1:
                h.next = h.next.next if h.next.next else None
            else:
                h = h.next

        return dummy.next
