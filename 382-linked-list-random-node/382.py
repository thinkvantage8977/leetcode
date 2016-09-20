# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
import random


class Solution(object):

    def __init__(self, head):
        self.head = head

    def getRandom(self):
        c = ans= 0
        node = self.head

        while node:
            
            if random.randint(0, c) == 0:
                ans = node.val
            node = node.next
            c += 1

        return ans


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()
