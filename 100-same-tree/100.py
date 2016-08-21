# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):

    def inOrderCompare(self, p, q):
        if p == None == q:
            return True
        if p and not q:
            return False
        if q and not p:
            return False
        if p.val == q.val:
            return self.inOrderCompare(p.left, q.left) and self.inOrderCompare(p.right, q.right)
        else:
            return False

    def isSameTree(self, p, q):
        return self.inOrderCompare(p, q)
