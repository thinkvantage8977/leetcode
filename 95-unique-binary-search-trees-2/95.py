# Definition for a binary tree node.
class TreeNode(object):

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):

    def generate(self, begin, end):
        res = []

        if begin > end:
            return [None]

        for i in range(begin, end + 1):
            left = self.generate(begin, i - 1)
            right = self.generate(i + 1, end)

            for l in left:
                for r in right:
                    node = TreeNode(i)
                    node.left = l
                    node.right = r
                    res.append(node)
        return res

    def generateTrees(self, n):
        if n == 0:
            return []
        return self.generate(1, n)
