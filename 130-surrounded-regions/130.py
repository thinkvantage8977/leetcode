class Solution(object):

    def dfs(self, i, j):
        if i < 0 or i >= self.n or j < 0 or j >= self.m:
            return

        if self.visited[i][j] == 1:
            return

        if self.board[i][j] == "X":
            return

        if self.board[i][j] == "O":
            self.visited[i][j] = 1
            self.board[i] = self.board[i][:j] + "k" + self.board[i][j + 1:]
            self.dfs(i + 1, j)
            self.dfs(i - 1, j)
            self.dfs(i, j + 1)
            self.dfs(i, j - 1)

    def solve(self, board):
        if not board or not board[0]:
            return board

        self.board = board
        self.m = len(board[0])
        self.n = len(board)

        self.visited = [[0 for i in range(len(board[0]))]for j in range(len(board))]

        for j in range(self.m):
            self.dfs(0, j)
            self.dfs(self.n - 1, j)

        for i in range(self.n):
            self.dfs(i, 0)
            self.dfs(i, self.m - 1)
        print(board)
        for i in range(self.n):
            for j in range(self.m):
                if self.board[i][j] == "k":
                    self.board[i] = self.board[i][:j] + "O" + self.board[i][j + 1:]
                elif self.board[i][j] == "O":
                    self.board[i] = self.board[i][:j] + "X" + self.board[i][j + 1:]


testClass = Solution()


board = ["XXXX", "XOOX", "XXOX", "XOXX"]
board = ["O"]



testClass.solve(board)

print(board)
