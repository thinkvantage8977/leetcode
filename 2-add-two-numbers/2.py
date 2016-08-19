
class ListNode(object):
	def __init__(self, x):
		self.val = x
		self.next = None

#Solution Class
class Solution(object):

	def carryList(self,l1):
		while l1.next != None:
			if l1.val >= 10:
				l1.next.val += l1.val // 10
				l1.val = l1.val % 10
			l1= l1.next
		if l1.next == None and l1.val >= 10:
			l1.next = ListNode(l1.val // 10)
			l1.val = l1.val % 10


	def reverseListNode(self,l1):
		result = ListNode(l1.val)
		while l1.next != None:
			l1 = l1.next
			newNode = ListNode(l1.val)
			newNode.next=result
			result=newNode
		return result
		
	def addTwoReversedListNode(self,l1,l2):
		newList = ListNode(l1.val+l2.val)
		head = newList

		while l1.next != None or l2.next!= None:
			sum = 0
			if l1.next:
				sum = sum + l1.next.val
				l1 = l1.next
			if l2.next:
				sum = sum + l2.next.val
				l2 = l2.next
			newList.next = ListNode(sum)
			newList = newList.next
		
		return head

	def addTwoNumbers(self, l1, l2):
		#rl1 = self.reverseListNode(l1)
		#rl2 = self.reverseListNode(l2)
		result = self.addTwoReversedListNode(l1,l2)
		

		#newresult = self.reverseListNode(result)

		self.carryList(result)

		return result
		


#Setup testClass
testClass = Solution()

#Test input
l1 = ListNode(2)
head1 = l1

l1.next = ListNode(4)
l1 = l1.next

l1.next = ListNode(9)
l1 = l1.next


l2 = ListNode(1)
head2 = l2

l2.next = ListNode(6)
l2 = l2.next

l2.next = ListNode(3)
l2 = l2.next


#Run
result = testClass.addTwoNumbers(head1,head2)

#Print

while result.next != None:
	print(result.val,"->", end="")
	result = result.next

print(result.val)