# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):

    def isUnival(self, root):
        if not root:
            return True

        resultLeft = self.isUnival(root.left)
        resultRight = self.isUnival(root.right)
        if resultLeft and resultRight:
            if root.left and root.left.val != root.val:
                return False
            if root.right and root.right.val != root.val:
                return False

            self.counter += 1
            return True

        return False

    def countUnivalSubtrees(self, root):
        self.counter = 0

        self.isUnival(root)
        return self.counter
