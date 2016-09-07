# Definition for singly-linked list with a random pointer.
# class RandomListNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None


class Solution(object):

    def DFSCopy(self, root):
        if root == None:
            return None

        if root in self.d:
            return self.d[root]

        node = RandomListNode(root.label)
        self.d[root] = node
        node.next = self.DFSCopy(root.next)

        node.random = self.DFSCopy(root.random)
        return node

    def copyRandomList(self, head):
        self.d = {}
        node = self.DFSCopy(head)
        return node
