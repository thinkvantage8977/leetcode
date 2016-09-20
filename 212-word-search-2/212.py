import collections


class triesNode(object):

    def __init__(self):
        self.isWord = False
        self.children = collections.defaultdict(triesNode)


class tries(object):

    def __init__(self):
        self.root = triesNode()

    def addWord(self, word):
        node = self.root
        for c in word:
            node = node.children[c]
        node.isWord = True

    def searchWord(self, word, isWord=True):
        node = self.root
        for c in word:
            if c not in node.children:
                return False
            node = node.children[c]
        return node.isWord if isWord else True


class Solution(object):

    def DFS(self, i, j, l, triesNode):

        if self.board[i][j] not in triesNode.children:
            return

        self.marker[i][j] = 1

        newl = l + self.board[i][j]

        if triesNode.children[self.board[i][j]].isWord and newl not in self.res:
            self.res.append(newl)

        if i + 1 < self.n and self.marker[i + 1][j] == 0:
            self.DFS(i + 1, j, newl, triesNode.children[self.board[i][j]])

        if j + 1 < self.m and self.marker[i][j + 1] == 0:
            self.DFS(i, j + 1, newl, triesNode.children[self.board[i][j]])

        if i - 1 >= 0 and self.marker[i - 1][j] == 0:
            self.DFS(i - 1, j, newl, triesNode.children[self.board[i][j]])

        if j - 1 >= 0 and self.marker[i][j - 1] == 0:
            self.DFS(i, j - 1, newl, triesNode.children[self.board[i][j]])

        self.marker[i][j] = 0

    def findWords(self, board, words):
        self.tries = tries()
        self.res = []
        self.board = board
        self.m = len(board[0])
        self.n = len(board)

        self.marker = [[0 for i in range(len(board[0]))] for j in range(len(board))]

        for w in words:
            self.tries.addWord(w)

        for i in range(self.n):
            for j in range(self.m):
                self.DFS(i, j, "", self.tries.root)

        return self.res


words = ["oath", "pea", "eat", "rain"]

board = ["oaan", "etae", "ihkr", "iflv"]


testClass = Solution()
print(testClass.findWords(board, words))
