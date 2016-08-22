# Definition for a binary tree node.
class TreeNode(object):

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):

    def levelOrder(self, root):
        result = []

        if not root:
            return []

        current_level = [root]
        next_level = []
        while current_level:
            next_level = []
            current_val = []
            for i in current_level:
                if i.left:
                    next_level.append(i.left)
                if i.right:
                    next_level.append(i.right)
                current_val.append(i.val)
            result.append(current_val)
            current_level = next_level

        return result


Head = TreeNode(1)
Head.left = TreeNode(9)
Head.right = TreeNode(20)
Head.right.left = TreeNode(15)
Head.right.right = TreeNode(7)


testClass = Solution()
print(testClass.levelOrder(Head))
