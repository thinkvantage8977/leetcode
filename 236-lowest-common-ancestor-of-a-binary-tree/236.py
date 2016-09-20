# 定义两个辅助节点，使用后续遍历来遍历整个树
# 当root的值等于p或者q时，找到一个符合条件的节点，返回这个root
# 先遍历左子树
# 再遍历右子树
# 当left，right均找到时返回此root
# 只找到left时返回left
# 只找到right时返回right
# 否则返回null

class Solution(object):

    def lowestCommonAncestor(self, root, p, q):
        if not root or root == p or root == q:
            return root

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if left and right:
            return root

        return left if left else right
