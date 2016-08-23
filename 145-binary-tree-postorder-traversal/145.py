# Definition for a binary tree node.
class TreeNode(object):

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    result = []

    def postorderTaversalToArray(self, node):
        if not node:
            return
        self.postorderTaversalToArray(node.left)
        self.postorderTaversalToArray(node.right)
        self.result.append(node.val)
        return

    def postorderTraversal(self, root):
        self.result = []
        self.postorderTaversalToArray(root)
        return self.result


Head = TreeNode(1)
# Head.left = TreeNode(5)
Head.right = TreeNode(2)
Head.right.left = TreeNode(3)
# Head.right.right = TreeNode(20)


testClass = Solution()
print(testClass.postorderTraversal(Head))
