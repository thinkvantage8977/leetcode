# Definition for singly-linked list.
class ListNode(object):

    def __init__(self, x):
        self.val = x
        self.next = None

# Definition for a binary tree node.


class TreeNode(object):

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):

    def BuildBinaryTree(self, node, val):
        if node.val > val:
            if not node.left:
                node.left = TreeNode(val)
            else:
                self.BuildBinaryTree(node.left, val)

        if node.val < val:
            if not node.right:
                node.right = TreeNode(val)
            else:
                self.BuildBinaryTree(node.right, val)


    def sortedListToBST(self, head):
    	h = head
    	slow,fast =head,head

    	while fast and fast.next:
    		fast = fast.next.next
    		slow = slow.next

    	treeNodeHead = TreeNode(slow.val)
    	fast = h

    	while slow.next:
    		BuildBinaryTree(treeNodeHead,slow.next.val)
    		BuildBinaryTree(treeNodeHead,)
