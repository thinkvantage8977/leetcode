# Definition for a binary tree node.
class TreeNode(object):

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    treeDict = {}
    maxDepth = 0

    def preOrderTraversal(self, node, l):
        if not node:
            return
        if l > self.maxDepth:
            self.maxDepth = l
        if l in self.treeDict:
            self.treeDict[l].append(node.val)
        else:
            self.treeDict[l] = [node.val]
        self.preOrderTraversal(node.left, l + 1)
        self.preOrderTraversal(node.right, l + 1)
        return

    def levelOrderBottom(self, root):
        if not root:
            return []
        self.treeDict = {}
        self.maxDepth = 0
        self.preOrderTraversal(root, 0)
        result = []
        for i in range(0, self.maxDepth + 1):
            result.append(self.treeDict[i])
        return result[::-1]


Head = TreeNode(1)
# Head.left = TreeNode(9)
# Head.right = TreeNode(20)
# Head.right.left = TreeNode(15)
# Head.right.right = TreeNode(7)


testClass = Solution()
print(testClass.levelOrderBottom(Head))
