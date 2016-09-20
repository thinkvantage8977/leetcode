

# Definition for a binary tree node.
class TreeNode(object):

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):

    def InOrderTraversal(self, root):
        if not root:
            return
        self.InOrderTraversal(root.left)

        if len(self.q) < self.k:
            self.q = [root.val] + self.q
        else:
            if abs(self.q[-1] - self.target) > abs(root.val - self.target):
                self.q.pop()
                self.q = [root.val] + self.q
            else:
                return

        self.InOrderTraversal(root.right)

    def closestKValues(self, root, target, k):
        self.q = []
        self.k = k
        self.target = target
        self.InOrderTraversal(root)
        return self.q
