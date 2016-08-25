# Definition for a binary tree node.
class TreeNode(object):

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    result = []

    def BFS(self, l):
        f = 0
        while l:
            nextLevel = []
            for n in l:
                if n.left:
                    nextLevel.append(n.left)
                if n.right:
                    nextLevel.append(n.right)
            valArray = []
            for i in l:
                valArray.append(i.val)
            # print(valArray)
            if f == 0:
                self.result.append(valArray)
            else:
                self.result.append(valArray[::-1])
            f = (f + 1) % 2
            l = nextLevel

    def zigzagLevelOrder(self, root):
        if not root:
            return []
        self.result = []
        self.BFS([root])
        return self.result


Head = TreeNode(3)
Head.left = TreeNode(9)

Head.right = TreeNode(20)
Head.right.left = TreeNode(15)
Head.right.right = TreeNode(7)

# Head.right.left = TreeNode(15)
# Head.right.right = TreeNode(7)


testClass = Solution()
print(testClass.zigzagLevelOrder(Head))
