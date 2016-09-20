

import heapq

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

    def mergeKLists(self, lists):
        if not lists:
            return
        
        h = []

        for l in lists:
            if l:
                heapq.heappush(h, (l.val, l))

        dummy = ListNode(-1)
        head = dummy
        while h:
            smallestNode = heapq.heappop(h)
            head.next = smallestNode[1]
            head = head.next
            if smallestNode[1].next:
                heapq.heappush(h, (smallestNode[1].next.val, smallestNode[1].next))

        return dummy.next


Head = ListNode(1)


testClass=  Solution()

node =testClass.mergeKLists([None,Head])


printList(node)