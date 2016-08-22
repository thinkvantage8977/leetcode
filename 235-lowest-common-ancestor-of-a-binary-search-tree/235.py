# Definition for a binary tree node.
class TreeNode(object):

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):

    def searchForLowestCommonAncestor(self, root, p, q):
        if not root:
            return None
        if root.val >= p.val and root.val <= q.val:
            return root
        if root.val <= p.val and root.val >= q.val:
            return root

        if root.val > p.val and root.val > q.val:
            return self.searchForLowestCommonAncestor(root.left, p, q)

        if root.val < p.val and root.val < q.val:
            return self.searchForLowestCommonAncestor(root.right, p, q)

    def lowestCommonAncestor(self, root, p, q):
        if not root:
            return None

        return self.searchForLowestCommonAncestor(root, p, q)


Head = TreeNode(6)

Head.left = TreeNode(2)
Head.right = TreeNode(8)

Head.left.left = TreeNode(0)
Head.left.right = TreeNode(4)


Head.left.right.left = TreeNode(3)
Head.left.right.right = TreeNode(5)

Head.right.left = TreeNode(7)
Head.right.left = TreeNode(9)


testClass = Solution()
print(testClass.lowestCommonAncestor(Head, Head.left, Head.left.right).val)
