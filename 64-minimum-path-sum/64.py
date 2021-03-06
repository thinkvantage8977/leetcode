class Solution(object):

    def minPathSum(self, grid):

        if not grid or not grid[0]:
            return 0

        for i in range(1, len(grid[0])):
            grid[0][i] += grid[0][i - 1]

        for i in range(1, len(grid)):
            grid[i][0] += grid[i - 1][0]

        for i in range(1, len(grid)):
            for j in range(1, len(grid[0])):
                grid[i][j] += min(grid[i - 1][j], grid[i][j - 1])

        return grid[len(grid) - 1][len(grid[0]) - 1]


testClass = Solution()

grid = [[1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [
    1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5]]

print(testClass.minPathSum(grid))
