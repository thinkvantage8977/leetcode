# Definition for binary tree with next pointer.
class TreeLinkNode(object):

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None


class Solution(object):

    def BFS(self, l):
        currentLevel = l
        while currentLevel:
            nextLevel = []
            for i in range(0, len(currentLevel) - 1):
                currentLevel[i].next = currentLevel[i + 1]
            l[len(l) - 1].next = None
            for n in currentLevel:
                if n.left:
                    nextLevel.append(n.left)
                if n.right:
                    nextLevel.append(n.right)
            currentLevel = nextLevel




    def connect(self, root):
        if root:
            self.BFS([root])
