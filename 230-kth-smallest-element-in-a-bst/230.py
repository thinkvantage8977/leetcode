# Definition for a binary tree node.
class TreeNode(object):

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    count = 0
    kth = 0
    result = None

    def inorderTraversalToArray(self, node):
        if not node or self.count == self.kth:
            return
        self.inorderTraversalToArray(node.left)
        self.count += 1
        if self.count == self.kth:
            self.result = node
            return
        self.inorderTraversalToArray(node.right)

    def kthSmallest(self, root, k):
        self.kth = k
        self.result = None
        self.count = 0
        self.inorderTraversalToArray(root)

        return self.result.val

Head = TreeNode(10)
Head.left = TreeNode(5)
Head.right = TreeNode(15)
Head.right.left = TreeNode(12)
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
print(testClass.kthSmallest(Head,4))