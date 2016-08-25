# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    nodes = [None, None]
    count = 0

    def DFS(self, root):
        if not root or self.count == 2:
            return

        if root.left and root.left.val >= root.val:
            self.nodes[self.count] = root.left
            self.count += 1

        self.DFS(root.left)

        if root.right and root.right.val < root.val:
            self.nodes[self.count] = root.right
            self.count += 1

        self.DFS(root.right)

    def recoverTree(self, root):
        if not root:
            return

        self.nodes = [None, None]
        self.count = 0
        self.DFS(root)
        a = self.nodes[0].val
        self.nodes[0].val = self.nodes[1].val
        self.nodes[1].val = a
