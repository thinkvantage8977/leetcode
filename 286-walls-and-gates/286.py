class Solution(object):

    def dfs(self, step, i, j):

        if i >= len(self.rooms) or i < 0 or j >= len(self.rooms[0]) or j < 0:
            return

        if self.rooms[i][j] == -1 or self.rooms[i][j] == 0:
            return

        if self.visited[i][j] == 1:
            return

        if self.rooms[i][j] > step:
            self.rooms[i][j] = step
            self.visited[i][j] = 1
            self.dfs(step + 1, i + 1, j)
            self.dfs(step + 1, i - 1, j)
            self.dfs(step + 1, i, j + 1)
            self.dfs(step + 1, i, j - 1)
            self.visited[i][j] = 0

    def wallsAndGates(self, rooms):
        if not rooms:
            return None

        if not rooms[0]:
            return []

        self.visited = [[0 for j in range(len(rooms[0]))] for i in range(len(rooms))]
        self.rooms = rooms

        for i in range(len(rooms)):
            for j in range(len(rooms[0])):
                if rooms[i][j] == 0:
                    self.visited[i][j] = 1
                    self.dfs(1, i + 1, j)
                    self.dfs(1, i - 1, j)
                    self.dfs(1, i, j + 1)
                    self.dfs(1, i, j - 1)
                    self.visited[i][j] = 0


m = [[2147483647, -1, 0, 2147483647], [2147483647, 2147483647, 2147483647, -1], [2147483647, -1, 2147483647, -1], [0, -1, 2147483647, 2147483647]]

testClass = Solution()

testClass.wallsAndGates(m)

print(m)
