# Definition for a binary tree node.
class TreeNode(object):

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):

    def compareDepth(self, node):

        left = node.left
        right = node.right
        l = 1
        while left and right:
            l += 1
            left = left.left
            right = right.right

        if left or right:
            return -1
        else:
            return l

    def countNodes(self, root):
        if not root:
            return 0
        l = self.compareDepth(root)
        if l != -1:
            return (2**l) - 1
        else:
            return self.countNodes(root.left) + self.countNodes(root.right) + 1


Head = TreeNode(1)
Head.left = TreeNode(2)


testClass = Solution()
print(testClass.countNodes(Head))
