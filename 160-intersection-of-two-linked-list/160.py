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
	def getIntersectionNode(self, headA, headB):
		l1 = headA
		l2 = headB
		c1 = 0
		c2 = 0
		while l1:
			c1+=1
			l1=l1.next
		while l2:
			c2+=1
			l2=l2.next

		l1 = headA
		l2 = headB

		if c1>c2:
			while c1!=c2:
				l1 = l1.next
				c1 -=1
		else:
			while c2!=c1:
				l2 = l2.next
				c2 -=1
 		
 		while l1 and l2:
 			if l1==l2:
 				return l1
 			l1=l1.next
 			l2=l2.next

 		return None
