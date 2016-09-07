class Solution(object):

    def uniquePathsWithObstacles(self, obstacleGrid):
        if not obstacleGrid or not obstacleGrid[0]:
            return 0
        w = len(obstacleGrid[0])
        l = len(obstacleGrid)

        dp = [[0 for i in range(w)] for j in range(l)]

        for i in range(l):
            for j in range(w):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                else:
                    if i == 0 and j == 0:
                        dp[i][j] = 1
                    elif i == 0:
                        if obstacleGrid[0][j - 1] == 1:
                            dp[i][j] = 0
                        else:
                            dp[i][j] = dp[i][j - 1]
                    elif j == 0:
                        if obstacleGrid[i - 1][0] == 1:
                            dp[i][j] = 0
                        else:
                            dp[i][j] = dp[i - 1][j]
                    else:
                        a = dp[i - 1][j] if obstacleGrid[i - 1][j] != 1 else 0
                        b = dp[i][j - 1] if obstacleGrid[i][j - 1] != 1 else 0
                        dp[i][j] = a + b
        # print(dp)
        return dp[-1][-1]


testClass = Solution()

l = [[0,0,0],[0,1,0],[0,0,0]]

print(testClass.uniquePathsWithObstacles(l))