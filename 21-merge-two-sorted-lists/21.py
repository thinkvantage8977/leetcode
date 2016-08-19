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
	#print(l.val)

class Solution(object):
	def mergeTwoLists(self, l1, l2):
		head = ListNode(0)
		l = head

		while l1 and l2:
			if l1.val < l2.val:
				l.next = l1
				l1 = l1.next
			else:
				l.next = l2
				l2 = l2.next
				
			l=l.next

		l.next = l1 or l2

		return head.next



testClass = Solution()

Head = ListNode(0)
Head.next = ListNode(2)
Head.next.next = ListNode(4)
Head.next.next.next = ListNode(6)
Head.next.next.next.next = ListNode(8)
Head.next.next.next.next.next = ListNode(10)
#Head.next.next.next.next.next.next = ListNode()


Head2 = ListNode(1)
Head2.next = ListNode(3)
Head2.next.next = ListNode(5)
Head2.next.next.next = ListNode(7)
Head2.next.next.next.next = ListNode(9)
Head2.next.next.next.next.next = ListNode(11)
#Head2.next.next.next.next.next.next = ListNode("7")

#printList(Head)
#printList(Head2)

print(printList(testClass.mergeTwoLists(Head,Head2)))