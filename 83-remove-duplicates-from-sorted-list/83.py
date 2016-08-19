# Definition for singly-linked list.
class ListNode(object):
	def __init__(self, x):
		self.val = x
		self.next = None

def printList(l):
	while l!=None:
		print(l.val, end="")
		if l.next:
			print('->', end="")
		l=l.next
	print()


class Solution(object):
    def deleteDuplicates(self, head):
        newL = ListNode(0)
        h = newL
        if not head:
        	return head

        current = head.val

        while head:
        	if current != head.val:
        		h.next = ListNode(current)
        		current = head.val
        		h = h.next
        	head = head.next

        h.next = ListNode(current)
        return newL.next


Head = ListNode(1)
Head.next = ListNode(1)
#Head.next.next = ListNode(2)
#Head.next.next.next = ListNode(4)
#Head.next.next.next.next = ListNode(5)
#Head.next.next.next.next.next = ListNode(5)
#Head.next.next.next.next.next.next = ListNode(7)
#Head.next.next.next.next.next.next.next = ListNode(8)
#Head.next.next.next.next.next.next.next.next = Head.next.next.next.next.next



testClass= Solution()

print(printList(testClass.deleteDuplicates(Head)))