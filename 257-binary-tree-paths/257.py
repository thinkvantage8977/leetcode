# Definition for a binary tree node.
class TreeNode(object):

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    result = []

    def DFSPath(self, root, s):
        if not root.left and not root.right:
            self.result.append(s)
        if root.left:
            self.DFSPath(root.left, s + "->" + str(root.left.val))
        if root.right:
            self.DFSPath(root.right, s + "->" + str(root.right.val))

    def binaryTreePaths(self, root):
        self.result = []
        if not root:
            return []
        else:
            self.DFSPath(root, str(root.val))
        return self.result

Head = TreeNode(1)
Head.left = TreeNode(2)
Head.right = TreeNode(3)

Head.left.left = TreeNode(4)
Head.left.right = TreeNode(5)

# Head.left.left.left = TreeNode(8)
# Head.left.left.right = TreeNode(9)


# Head.left.right.left = TreeNode(9)
# Head.left.right.right = TreeNode(8)

Head.right.left = TreeNode(6)
Head.right.right = TreeNode(7)
# Head.right.right = TreeNode(7)


testClass = Solution()
print(testClass.binaryTreePaths(None))
