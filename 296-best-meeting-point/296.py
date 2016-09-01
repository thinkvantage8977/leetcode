class Solution(object):

    def minTotalDistance(self, grid):
        x = []
        y = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    x.append(i)
                    y.append(j)

        x.sort()
        y.sort()
        mid = len(x) // 2
        d = 0

        for i in x:
            d += abs(x[mid] - i)

        for i in y:
            d += abs(y[mid] - i)

        return d
