# Definition for a binary tree node.
class TreeNode(object):

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):

    def DFSSum(self, node, sum, current):
        current += node.val
        if not node.left and not node.right:
            print("node.val = {}, current = {}, sum = {}".format(
                node.val, current, sum))
            print(sum == current)
            if sum == current:
                return True
            else:
                return False
        left = False
        if node.left:
            left = self.DFSSum(node.left, sum, current)

        right = False
        if node.right:
            right = self.DFSSum(node.right, sum, current)

        return left or right

    def hasPathSum(self, root, sum):
        if not root:
            return False
        return self.DFSSum(root, sum, 0)


Head = TreeNode(1)
Head.left = TreeNode(-2)
Head.right = TreeNode(3)
# Head.right.left = TreeNode(15)
# Head.right.right = TreeNode(7)


testClass = Solution()
print(testClass.hasPathSum(Head, -1))
