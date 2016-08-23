# Definition for a binary tree node.
class TreeNode(object):

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):

    def inOrderTraverseValidation(self, node, maxNode, minNode):
        if not node:
            return True

        print("Node.val = {}, max = {}, min = {}".format(
            node.val, maxNode, minNode))

        if node.val <= minNode or node.val >= maxNode:
            return False
        return self.inOrderTraverseValidation(node.left, node.val, minNode) and self.inOrderTraverseValidation(node.right, maxNode, node.val)

    def isValidBST(self, root):
        return self.inOrderTraverseValidation(root, float("inf"), -float("inf"))

Head = TreeNode(10)
Head.left = TreeNode(5)
Head.right = TreeNode(15)
Head.right.left = TreeNode(6)
Head.right.right = TreeNode(20)


# Head.left.left = TreeNode(4)
# Head.left.right = TreeNode(5)

# Head.left.left.left = TreeNode(8)
# Head.left.left.right = TreeNode(9)


# Head.left.right.left = TreeNode(9)
# Head.left.right.right = TreeNode(8)

# Head.right.left = TreeNode(5)
# Head.right.right = TreeNode(4)
# Head.right.right = TreeNode(7)


testClass = Solution()
print(testClass.isValidBST(Head))
