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
	def detectCycle(self, head):
		
		p1 = head
		p2 = head

		while p2 and p2.next and p2.next.next:
			p1=p1.next
			p2=p2.next.next

			if p1 == p2:
				break

		if not p2 or not p2.next or not p2.next.next:
			return None

		p1 = head

		while p1!=p2:
			p1=p1.next
			p2=p2.next

		return p1
		

Head = ListNode(1)
Head.next = ListNode(2)
Head.next.next = ListNode(3)
Head.next.next.next = ListNode(4)
Head.next.next.next.next = ListNode(5)
Head.next.next.next.next.next = ListNode(6)
Head.next.next.next.next.next.next = ListNode(7)
Head.next.next.next.next.next.next.next = ListNode(8)
Head.next.next.next.next.next.next.next.next = Head.next.next.next.next.next



testClass= Solution()

print(testClass.hasCycle(None))