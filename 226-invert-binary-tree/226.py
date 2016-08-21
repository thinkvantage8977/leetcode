# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):

    def swapTree(self, node):
        if not node:
            return

        self.swapTree(node.left)
        self.swapTree(node.right)
        a = node.right
        node.right = node.left
        node.left = a

        return

    def invertTree(self, root):
        self.swapTree(root)
        return root
