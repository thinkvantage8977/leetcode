class Solution(object):

    def numberOfPatterns(self, m, n):
        dp = [[1, 1, 1, 1, 1, 1, 1, 1, 1] for i in range(n)]
        dp[1] = [3, 5, 3, 5, 8, 5, 3, 5, 3]

        for i in range(2, n):
            dp[i][0] = dp[i - 1][1] + dp[i - 1][3] + dp[i - 1][4]

            dp[i][1] = dp[i - 1][0] + dp[i - 1][3] + dp[i - 1][4] + dp[i - 1][5] + dp[i - 1][2]

            dp[i][2] = dp[i - 1][1] + dp[i - 1][4] + dp[i - 1][5]

            dp[i][3] = dp[i - 1][0] + dp[i - 1][1] + dp[i - 1][4] + dp[i - 1][7] + dp[i - 1][6]

            dp[i][4] = dp[i - 1][0] + dp[i - 1][1] + dp[i - 1][2] + dp[i - 1][3] + dp[i - 1][5] + dp[i - 1][6] + dp[i - 1][7] + dp[i - 1][8]

            dp[i][5] = dp[i - 1][2] + dp[i - 1][1] + dp[i - 1][4] + dp[i - 1][7] + dp[i - 1][8]

            dp[i][6] = dp[i - 1][3] + dp[i - 1][4] + dp[i - 1][7]

            dp[i][7] = dp[i - 1][6] + dp[i - 1][3] + dp[i - 1][4] + dp[i - 1][5] + dp[i - 1][8]

            dp[i][8] = dp[i - 1][4] + dp[i - 1][5] + dp[i - 1][7]

            dp[i][0] += dp[i - 2][2] + dp[i - 2][5] + dp[i - 2][8] + dp[i - 2][7] + dp[i - 2][6]

            dp[i][1] += dp[i - 2][6] + dp[i - 2][7] + dp[i - 2][8]

            dp[i][2] += dp[i - 2][0] + dp[i - 2][3] + dp[i - 2][6] + dp[i - 2][7] + dp[i - 2][8]

            dp[i][3] += dp[i - 2][2] + dp[i - 2][5] + dp[i - 2][8]

            dp[i][5] += dp[i - 2][0] + dp[i - 2][3] + dp[i - 2][6]

            dp[i][6] += dp[i - 2][0] + dp[i - 2][1] + dp[i - 2][2] + dp[i - 2][5] + dp[i - 2][8]

            dp[i][7] += dp[i - 2][0] + dp[i - 2][1] + dp[i - 2][2]

            dp[i][8] += dp[i - 2][6] + dp[i - 2][3] + dp[i - 2][0] + dp[i - 2][1] + dp[i - 2][2]

        total = 0

        print(dp)

        for i in range(m - 1, n):
            total += sum(dp[i])
        return total


testClass = Solution()

print(testClass.numberOfPatterns(1, 2))
