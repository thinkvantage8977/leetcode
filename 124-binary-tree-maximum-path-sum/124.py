# Definition for a binary tree node.
class TreeNode(object):

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):

    def postOrderTravserse(self, node):
        if not node:
            return 0
        left = self.postOrderTravserse(node.left)
        right = self.postOrderTravserse(node.right)
        onePath = node.val
        if left > 0:
            onePath += left
        if right > 0:
            onePath += right

        self.maxSum = max(self.maxSum, onePath)
        return max(node.val, node.val + left, node.val + right)

    def maxPathSum(self, root):
        self.maxSum = -float("inf")
        self.postOrderTravserse(root)
        return self.maxSum


Head = TreeNode(1)
Head.left = TreeNode(2)
Head.right = TreeNode(3)

# Head.left.left = TreeNode(4)
# Head.left.right = TreeNode(5)

testClass = Solution()


print(testClass.maxPathSum(Head))
