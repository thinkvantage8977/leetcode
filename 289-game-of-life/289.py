class Solution(object):

    def exist(self, i, j, board):
        m = len(board[0])
        n = len(board)
        if i < 0 or i >= n or j < 0 or j >= m:
            return 0
        return board[i][j]

    def gameOfLife(self, board):
        m = len(board[0])
        n = len(board)
        nextG = [[0 for i in range(m)] for j in range(n)]

        for i in range(n):
            for j in range(m):
                neighbor = self.exist(i - 1, j - 1, board) + self.exist(i - 1, j, board) + self.exist(i - 1, j + 1, board) + self.exist(i, j - 1, board) + \
                    self.exist(i, j + 1, board) + self.exist(i + 1, j - 1, board) + self.exist(i + 1, j, board) + self.exist(i + 1, j + 1, board)

                print(neighbor)
                if board[i][j] == 1 and neighbor < 2:
                    nextG[i][j] = 0

                if board[i][j] == 1 and neighbor >= 2 and neighbor <= 3:
                    nextG[i][j] = 1

                if board[i][j] == 1 and neighbor > 3:
                    nextG[i][j] = 0

                if board[i][j] == 0 and neighbor == 3:
                    nextG[i][j] = 1

        for i in range(n):
            for j in range(m):
                board[i][j] = nextG[i][j]


testClass = Solution()


board = [[1]]

testClass.gameOfLife(board)

print(board)
