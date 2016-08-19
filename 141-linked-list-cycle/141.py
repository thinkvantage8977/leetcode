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
	def hasCycle(self, head):
		nodeSet = {}

		while head:
			if head not in nodeSet:
				nodeSet[head] = True
			else:
				return True
			head = head.next

		return False
		

Head = ListNode(1)
Head.next = ListNode(2)
Head.next.next = ListNode(3)
Head.next.next.next = ListNode(4)
Head.next.next.next.next = ListNode(5)
Head.next.next.next.next.next = ListNode(6)
Head.next.next.next.next.next.next = ListNode(7)
Head.next.next.next.next.next.next.next = ListNode(8)
#Head.next.next.next.next.next.next.next.next = Head.next.next.next.next.next



testClass= Solution()

print(testClass.hasCycle(Head))