class Solution(object):

    def coinChange(self, coins, amount):
        dp = [float("inf")] * (amount + 1)
        dp[0] = 0

        coins.sort()

        for i in range(amount + 1):
            for j in coins:
                if i >= j and dp[i - j] + 1 < dp[i]:
                    dp[i] = dp[i - j] + 1
        if dp[amount] == float("inf"):
            return -1
        return(dp[amount])


testClass = Solution()

print(testClass.coinChange([1, 2, 5], 11))
