class Solution(object):

    def DFS(self, i, j):
        if i >= self.n or i < 0 or j >= self.m or j < 0:
            return
        if self.grid[i][j] == "1":
            self.grid[i][j] = "0"
            self.DFS(i + 1, j)
            self.DFS(i - 1, j)
            self.DFS(i, j + 1)
            self.DFS(i, j - 1)
        return

    def numIslands(self, grid):
        if not grid:
            return 0
        self.n = len(grid)
        self.m = len(grid[0])
        counter = 0

        self.grid = grid[::]

        for i in range(self.n):
            for j in range(self.m):
                if self.grid[i][j] == "1":
                    counter += 1
                    self.DFS(i, j)

        return counter


testClass = Solution()

g = [[1, 1, 0, 0, 0],
     [1, 1, 0, 0, 0],
     [0, 0, 1, 0, 0],
     [0, 0, 0, 1, 1]]

print(testClass.numIslands(g))
