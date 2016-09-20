# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):

    def verticalOrder(self, root):
        if not root:
            return []
        self.d = {}

        currentLevel = [(0, root)]

        while currentLevel:
            nextLevel = []

            for i in currentLevel:
                if i[0] not in self.d:
                    self.d[i[0]] = [i[1].val]
                else:
                    self.d[i[0]].append(i[1].val)

                if i[1].left:
                    nextLevel.append((i[0] - 1, i[1].left))

                if i[1].right:
                    nextLevel.append((i[0] + 1, i[1].right))

            currentLevel=nextLevel

        temp = []
        for key, value in self.d.items():
            temp.append((key, value))
        temp.sort(key=lambda x: x[0])
        res = []
        for i in temp:
            res.append(i[1])

        return res
