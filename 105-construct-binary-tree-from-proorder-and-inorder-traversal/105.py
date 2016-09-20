# Definition for a binary tree node.
# 前序遍历第一个元素是根结点（k），在中序遍历序列中找值为k的下标idx，idx将中序遍历序列分成左右子树，对前序遍历序列也一样，可进行递归操作 
class TreeNode(object):

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):

    def buildTreeRecursive(self, prestart, preend, instart, inend):
        if prestart >= preend:
            return None

        node = TreeNode(self.preorder[prestart])

        offSet = self.inorder[instart:inend + 1].index(node.val)

        node.left = self.buildTreeRecursive(
            prestart + 1, prestart + offSet + 1, instart, instart + offSet)

        node.right = self.buildTreeRecursive(
            prestart + offSet + 1, preend, instart + offSet + 1, inend)

        return node

    def buildTree(self, preorder, inorder):
        if not preorder:
            return None
        self.preorder = preorder
        self.inorder = inorder
        return self.buildTreeRecursive(0, len(preorder), 0, len(inorder))
