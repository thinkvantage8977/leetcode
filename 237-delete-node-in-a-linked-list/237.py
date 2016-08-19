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
    def deleteNode(self, node):
       if node.next != None:
       	node.val = node.next.val
       	node.next = node.next.next
       else:
       	node = None