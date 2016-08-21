# Definition for a binary tree node.
class TreeNode(object):

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):

    def depthTraverse(self, node):
        
        if not node:
            return 0
        left_depth = self.depthTraverse(node.left)

        right_depth = self.depthTraverse(node.right)

        if abs(right_depth - left_depth) > 1:
            return float("inf")

        return max(right_depth, left_depth) + 1

    def isBalanced(self, root):
        if not root:
            return True

        depth = self.depthTraverse(root)

        return depth != float("inf")


Head = TreeNode(1)
Head.right = TreeNode(2)
Head.right.right = TreeNode(3)

# Head.right = TreeNode(20)
# Head.right.left = TreeNode(15)
# Head.right.left.left = TreeNode(15)
# Head.right.right = TreeNode(7)


testClass = Solution()
print(testClass.isBalanced(Head))
