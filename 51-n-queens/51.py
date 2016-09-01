class Solution(object):

    def updateResult(self, s):
        board = []
        for c in s:
            line = ["."] * self.n
            line[int(c)] = "Q"
            board.append("".join(line))
        self.solutions.append(board)

    def DFS(self, l, result):
        if l == self.n:
            self.updateResult(result)
            return
        for i in range(0, self.n):
            if self.vertical[i] == 0 and self.slash1[l + i] == 0 and self.slash2[l - i] == 0:
                self.vertical[i] = 1
                self.slash1[l + i] = 1
                self.slash2[l - i] = 1
                self.DFS(l + 1, result + str(i))
                self.vertical[i] = 0
                self.slash1[l + i] = 0
                self.slash2[l - i] = 0

    def solveNQueens(self, n):
        if n == 0:
            return []
        self.solutions = []
        self.n = n
        self.vertical = [0] * n
        self.slash1 = [0] * 2 * n
        self.slash2 = [0] * 2 * n
        self.DFS(0, "")
        return self.solutions


testClass = Solution()

print(testClass.solveNQueens(3))
