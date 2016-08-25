# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    treeSum = 0

    def DFS(self, root, parentSum):
        if not root.left and not root.right:
            self.treeSum += parentSum * 10 + root.val
            return
        if root.left:
            self.DFS(root.left, parentSum * 10 + root.val)
        if root.right:
            self.DFS(root.right, parentSum * 10 + root.val)
        return

    def sumNumbers(self, root):
        if not root:
            return 0
        self.treeSum = 0
        self.DFS(root, 0)
        return self.treeSum
