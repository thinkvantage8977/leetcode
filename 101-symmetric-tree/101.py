# Definition for a binary tree node.
class TreeNode(object):

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):

    def recursiveSymmetric(self, left, right):
        if not left or not right:
            return left == right
        if left.val != right.val:
            return False
        return self.recursiveSymmetric(left.left, right.right) and self.recursiveSymmetric(left.right, right.left)

    def isSymmetric(self, root):
        if not root:
            return True

        return self.recursiveSymmetric(root.left, root.right)

Head = TreeNode(2)
Head.left = TreeNode(3)
Head.right = TreeNode(3)

Head.left.left = TreeNode(4)
Head.left.right = TreeNode(5)

# Head.left.left.left = TreeNode(8)
# Head.left.left.right = TreeNode(9)


# Head.left.right.left = TreeNode(9)
# Head.left.right.right = TreeNode(8)

Head.right.left = TreeNode(5)
Head.right.right = TreeNode(4)
# Head.right.right = TreeNode(7)


testClass = Solution()
print(testClass.isSymmetric(Head))
