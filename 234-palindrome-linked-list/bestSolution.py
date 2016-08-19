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
	def isPalindrome(self, head):
		
		#Special Case
		if not head or not head.next:
			return True

		#Get the mid point
		slow = fast = cur = head
		
		while fast and fast.next:
			fast, slow = fast.next.next, slow.next

		#Push second half to a stack
		stack = [slow.val]

		while slow.next:
			slow= slow.next
			stack.append(slow.val)

		print(stack)

		#Compare stack
		while stack:
			if stack.pop() != cur.val:
				return False
			cur = cur.next

		return True 


		



Head = ListNode("1")
Head.next = ListNode("1")
Head.next.next = ListNode("3")
Head.next.next.next = ListNode("3")
Head.next.next.next.next = ListNode("2")
Head.next.next.next.next.next = ListNode("1")
Head.next.next.next.next.next.next = ListNode("4")


testClass= Solution()

print(testClass.isPalindrome(Head))