# Definition for a binary tree node.
class TreeNode(object):

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    max_depth = 0

    def traverse(self, node, l):
        if not node.left and not node.right:
            self.max_depth = max(l, self.max_depth)
            return
        if node.left:
            self.traverse(node.left, l + 1)
        if node.right:
            self.traverse(node.right, l + 1)

    def maxDepth(self, root):
        self.max_depth = 0
        if not root:
            return 0
        self.traverse(root, 1)
        return self.max_depth

Head = TreeNode(1)
Head.left = TreeNode(9)
Head.right = TreeNode(20)
Head.right.left = TreeNode(15)
Head.right.right = TreeNode(7)


testClass = Solution()
print(testClass.maxDepth(Head))
