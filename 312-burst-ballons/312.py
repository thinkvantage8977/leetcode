class Solution(object):

    def maxCoins(self, nums):
        newNums = [1] + nums + [1]
        dp = [[0 for i in range(len(newNums))] for j in range(len(newNums))]
        n = len(newNums)

        # length for current situation, we start from 2, so we will consider cases from (0,2) (1,3).....then (0,3) (1,4)
        for k in range(2, n):
                # Starting point like 0,1,2,3,.....
            for i in range(0, n - k):
                # iterate node between two points
                # So for k=5 (0,5) we will consider  (0,1)and(1,5) +n[0]*n[1]*n[5], then (0,2) and (2,5) + n[0]*n[2]*n[5]
                # At when k=5 we know we have iterated k=4,k=3,k=2 so
                # (0,2) (0,3) (0,4) must be filled already
                for j in range(i + 1, i + k):
                    dp[i][i + k] = max(dp[i][i + k], dp[i][j] + dp[j][i + k] + newNums[i] * newNums[j] * newNums[i + k])

        return dp[0][n - 1]


testClass = Solution()

l = [3, 1, 5, 8]

print(testClass.maxCoins(l))
