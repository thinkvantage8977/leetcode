# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    nodeList = []

    def preOrderTraversal(self, node):
        if not node:
            return
        self.nodeList.append(node)
        self.preOrderTraversal(node.left)
        self.preOrderTraversal(node.right)

    def flatten(self, root):
        if not root:
            return []
        self.nodeList = []
        self.preOrderTraversal(root)

        for i in range(0, len(self.nodeList) - 1):
            self.nodeList[i].left = None
            self.nodeList[i].right = self.nodeList[i + 1]

        self.nodeList[len(self.nodeList) - 1].left = None
        self.nodeList[len(self.nodeList) - 1].right = None
