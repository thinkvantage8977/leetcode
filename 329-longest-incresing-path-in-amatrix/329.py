# 记忆化搜索。
# 设dis[i][j]为当前点出发最大上升路径的值。初始设置为0，表示该点未知，需要更新。
# 再次碰到的时候只需要返回该值即可。

class Solution(object):

    def DFS(self, i, j, length, value):

        if self.marker[i][j] != 0:
            return self.marker[i][j]
        if i + 1 < self.n and value < self.matrix[i + 1][j]:
            self.marker[i][j] = max(self.marker[i][j], self.DFS(i + 1, j, length + 1, self.matrix[i + 1][j]))

        if j + 1 < self.m and value < self.matrix[i][j + 1]:
            self.marker[i][j] = max(self.marker[i][j], self.DFS(i, j + 1, length + 1, self.matrix[i][j + 1]))

        if i - 1 >= 0 and value < self.matrix[i - 1][j]:
            self.marker[i][j] = max(self.marker[i][j], self.DFS(i - 1, j, length + 1, self.matrix[i - 1][j]))

        if j - 1 >= 0 and value < self.matrix[i][j - 1]:
            self.marker[i][j] = max(self.marker[i][j], self.DFS(i, j - 1, length + 1, self.matrix[i][j - 1]))

        self.marker[i][j] += 1
        self.maxL = max(self.maxL, self.marker[i][j])
        return self.marker[i][j]

    def longestIncreasingPath(self, matrix):
        if not matrix:
            return 0

        self.matrix = matrix
        self.marker = [[0 for i in range(len(matrix[0]))] for j in range(len(matrix))]
        self.maxL = 0
        self.m = len(matrix[0])
        self.n = len(matrix)

        for i in range(self.n):
            for j in range(self.m):
                self.DFS(i, j, 1, self.matrix[i][j])

        return self.maxL


testClass = Solution()
m = [
    [9, 9, 4],
    [6, 6, 8],
    [2, 1, 1]
]

m = [
    [3, 4, 5],
    [3, 2, 6],
    [2, 2, 1]
]

print(testClass.longestIncreasingPath(m))
