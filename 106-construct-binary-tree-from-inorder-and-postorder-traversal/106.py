# Definition for a binary tree node.
class TreeNode(object):

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):

    def buildTreeRecrusive(self, poststart, postend, instart, inend):
        if poststart >= postend:
            return None

        node = TreeNode(self.postorder[postend - 1])

        offset = self.inorder[instart:inend].index(node.val)

        node.left = self.buildTreeRecrusive(
            poststart, poststart + offset, instart, instart + offset)

        node.right = self.buildTreeRecrusive(
            poststart + offset, postend - 1, instart + offset + 1, inend)

        return node

    def buildTree(self, inorder, postorder):
        if not inorder:
            return None

        self.inorder=inorder
        self.postorder = postorder
        
        return self.buildTreeRecrusive(0,len(postorder),0,len(inorder))


