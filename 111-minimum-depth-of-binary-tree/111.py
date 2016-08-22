# Definition for a binary tree node.
class TreeNode(object):

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    min_depth = 2147483648

    def traverse(self, root, l):
        if not root.left and not root.right and l < self.min_depth:
            self.min_depth = l
            return
        if root.left:
            self.traverse(root.left, l + 1)
        if root.right:
            self.traverse(root.right, l + 1)
        return

    def minDepth(self, root):
        if not root:
            return 0
        self.min_depth = 2147483648
        self.traverse(root, 1)
        return self.min_depth


Head = TreeNode(1)
# Head.left = TreeNode(9)
# Head.right = TreeNode(20)
# Head.right.left = TreeNode(15)
# Head.right.right = TreeNode(7)


testClass = Solution()
print(testClass.minDepth(None))
