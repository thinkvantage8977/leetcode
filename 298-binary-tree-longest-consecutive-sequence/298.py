# Definition for a binary tree node.
class TreeNode(object):

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):

    def DFS(self, node, pv, d):
        if not node:
            return

        if node.val - pv == 1:
            d += 1
            self.longest = max(self.longest, d)
        else:
            d = 1

        self.DFS(node.left, node.val, d)
        self.DFS(node.right, node.val, d)

    def longestConsecutive(self, root):
        self.longest = 1
        if not root:
            return 0
        self.DFS(root.left, root.val, 1)
        self.DFS(root.right, root.val, 1)
        return self.longest


testClass = Solution()


Head = TreeNode(1)
Head.right = TreeNode(3)
Head.right.right = TreeNode(4)
Head.right.right.right = TreeNode(5)
Head.right.left = TreeNode(2)


print(testClass.longestConsecutive(Head))
