# Definition for a binary tree node.
class TreeNode(object):

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    result = []

    def preorderTaversalToArray(self, node):
        if not node:
            return
        self.result.append(node.val)
        self.preorderTaversalToArray(node.left)
        self.preorderTaversalToArray(node.right)
        return

    def preorderTraversal(self, root):
        self.result = []
        self.preorderTaversalToArray(root)
        return self.result


Head = TreeNode(1)
# Head.left = TreeNode(5)
Head.right = TreeNode(2)
Head.right.left = TreeNode(3)
# Head.right.right = TreeNode(20)


testClass = Solution()
print(testClass.preorderTraversal(Head))
