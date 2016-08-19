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
	def reverseList(self, l):
		n = l
		reverse = None
		
		while n!= None:
			new= ListNode(n.val)
			new.next=reverse
			reverse = new
			n=n.next

		return reverse

	def isPalindrome(self, head):
		reverse = self.reverseList(head)
		h = head

		while h!=None:
			if h.val!=reverse.val:
				return False
			h=h.next
			reverse=reverse.next

		return True 


		



Head = ListNode("1")
Head.next = ListNode("2")
Head.next.next = ListNode("3")
Head.next.next.next = ListNode("3")
Head.next.next.next.next = ListNode("2")
Head.next.next.next.next.next = ListNode("1")
Head.next.next.next.next.next.next = ListNode("4")


testClass= Solution()

print(testClass.isPalindrome(Head))