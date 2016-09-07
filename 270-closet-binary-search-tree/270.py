# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):

    def InOrderT(self, root):
        if not root:
            return
        self.InOrderT(root.left)
        if root.val > self.target and abs(root.val - self.target) > self.minD[0]:
            return
        if abs(root.val - self.target) < self.minD[0]:
            self.minD = (abs(root.val - self.target), root.val)
        self.InOrderT(root.right)

    def closestValue(self, root, target):
        self.target = target
        self.minD = (float("inf"), -1)

        self.InOrderT(root)
        return self.minD[1]
