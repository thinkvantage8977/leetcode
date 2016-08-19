# Definition for singly-linked list.
class ListNode(object):
	def __init__(self, x):
		self.val = x
		self.next = None


def printList(l):
	while l.next!=None:
		print(l.val, end="")
		print('->', end="")
		l=l.next
	print(l.val)

class Solution(object):
	def removeNthFromEnd(self, head, n):
		p1 = head
		p2 = head
		
		for i in range(0,n):
			p2 = p2.next
		
		if not p2:
			head = head.next
			return head

		while p2.next:
			p1=p1.next
			p2=p2.next
		
		p1.next= p1.next.next

		return head



testClass = Solution()

Head = ListNode("1")
Head.next = ListNode("2")
Head.next.next = ListNode("3")
Head.next.next.next = ListNode("4")
Head.next.next.next.next = ListNode("5")
Head.next.next.next.next.next = ListNode("6")
Head.next.next.next.next.next.next = ListNode("7")


print(printList(testClass.removeNthFromEnd(Head,7)))
