class Solution(object):

    def DFS(self, i, j, l):
        if l == len(self.word):
            return True
        res = False

        if i - 1 >= 0 and self.board[i - 1][j] == self.word[l] and self.marker[i - 1][j] == 0:
            self.marker[i - 1][j] = 1
            res = self.DFS(i - 1, j, l + 1)
            self.marker[i - 1][j] = 0
            if res:
                return res

        if j - 1 >= 0 and self.board[i][j - 1] == self.word[l] and self.marker[i][j - 1] == 0:
            self.marker[i][j - 1] = 1
            res = self.DFS(i, j - 1, l + 1)
            self.marker[i][j - 1] = 0
            if res:
                return res

        if i + 1 < len(self.board) and self.board[i + 1][j] == self.word[l] and self.marker[i + 1][j] == 0:
            self.marker[i + 1][j] = 1
            res = self.DFS(i + 1, j, l + 1)
            self.marker[i + 1][j] = 0
            if res:
                return res

        if j + 1 < len(self.board[0]) and self.board[i][j + 1] == self.word[l] and self.marker[i][j + 1] == 0:
            self.marker[i][j + 1] = 1
            res = self.DFS(i, j + 1, l + 1)
            self.marker[i][j + 1] = 0
            if res:
                return res

        return res

    def exist(self, board, word):
        self.marker = [[0 for i in range(len(board[0]))] for j in range(len(board))]
        self.word = word
        self.board = board
        res = False
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    self.marker[i][j] = 1
                    res = self.DFS(i, j, 1)
                    self.marker[i][j] = 0
                    if res:
                        return res
        return res


testClass = Solution()

b = [
    ['A', 'B', 'C', 'E'],
    ['S', 'F', 'C', 'S'],
    ['A', 'D', 'E', 'E']
]

print(testClass.exist(b, "ABCB"))
