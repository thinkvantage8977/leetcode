# Definition for a binary tree node.
class TreeNode(object):

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    result = []

    def BFS(self, l):
        currentLevel = l
        while currentLevel:
            nextLevel = []
            for n in currentLevel:
                if n.left:
                    nextLevel.append(n.left)
                if n.right:
                    nextLevel.append(n.right)
            self.result.append(currentLevel.pop().val)
            currentLevel = nextLevel

    def rightSideView(self, root):
        self.result = []
        if root:
            self.BFS([root])
            return self.result
        else:
            return []


Head = TreeNode(1)
Head.left = TreeNode(2)
Head.right = TreeNode(3)
Head.left.right = TreeNode(5)
Head.right.right = TreeNode(4)


testClass = Solution()
print(testClass.rightSideView(Head))
