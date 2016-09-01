class Solution(object):

    def DFS(self, l):
        if l == self.n:
            self.count += 1
            return
        for i in range(0, self.n):
            if self.vertical[i] == 0 and self.slash1[l + i] == 0 and self.slash2[l - i] == 0:
                self.vertical[i] = 1
                self.slash1[l + i] = 1
                self.slash2[l - i] = 1
                self.DFS(l + 1)
                self.vertical[i] = 0
                self.slash1[l + i] = 0
                self.slash2[l - i] = 0

    def totalNQueens(self, n):
        self.count = 0
        self.n = n
        self.vertical = [0] * n
        self.slash1 = [0] * 2 * n
        self.slash2 = [0] * 2 * n
        self.DFS(0)
        return self.count


testClass = Solution()

print(testClass.totalNQueens(8))
