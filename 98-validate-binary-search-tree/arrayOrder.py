# Definition for a binary tree node.
class TreeNode(object):

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    arrayVal = []

    def inOrderTraverseValidation(self, node):
        if not node:
            return

        self.inOrderTraverseValidation(node.left)
        self.arrayVal.append(node.val)
        self.inOrderTraverseValidation(node.right)
        
        return

    def isValidBST(self, root):
        self.arrayVal = []
        self.inOrderTraverseValidation(root)
        print(self.arrayVal)

        for i in range(0, len(self.arrayVal) - 1):
            if self.arrayVal[i] >= self.arrayVal[i + 1]:
                return False
        return True

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
