# Definition for a binary tree node.
class TreeNode(object):

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    result = []

    def DFS(self, root, l, targetSum, current):

        # print("l = {}, targetSumm = {}, current = {}".format(l, targetSum, current))

        if not root.left and not root.right and root.val + current == targetSum:
            self.result.append(l + [root.val])
            return

        if root.left:
            self.DFS(root.left, l + [root.val], targetSum, current + root.val)

        if root.right:
            self.DFS(root.right, l + [root.val], targetSum, current + root.val)

    def pathSum(self, root, sum):
        if not root:
            return []

        self.result = []

        self.DFS(root, [], sum, 0)

        return self.result


Head = TreeNode(5)
Head.left = TreeNode(4)
Head.left.left = TreeNode(11)
Head.left.left.left = TreeNode(7)
Head.left.left.right = TreeNode(2)


Head.right = TreeNode(8)
Head.right.left = TreeNode(13)
Head.right.right = TreeNode(4)
Head.right.right.left = TreeNode(5)
Head.right.right.right = TreeNode(1)


# Head.right.left = TreeNode(15)
# Head.right.right = TreeNode(7)


testClass = Solution()
print(testClass.pathSum(Head, 22))
