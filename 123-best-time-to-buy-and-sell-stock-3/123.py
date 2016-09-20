class Solution(object):

    def maxProfit(self, prices):
        if not prices:
            return 0
        dp = [0] * len(prices)


        #Tread it as on transaction
        minSofar = prices[0]
        maxProfit = 0
        for i in range(1, len(prices)):
            minSofar = min(minSofar, prices[i])
            maxProfit = max(maxProfit, prices[i] - minSofar)
            dp[i] = maxProfit

        #If the first max happened [0-j] then the next must in [j-len(nums)]
        #So do a backward again
        dp1 = [0] * len(prices)
        maxSoFar = prices[-1]
        maxProfit = 0
        for i in range(len(prices) - 2, -1, -1):
            maxSoFar = max(maxSoFar, prices[i])
            maxProfit = max(maxProfit, maxSoFar - prices[i])
            dp1[i] = maxProfit

        maxTwoTrans = 0
        for i in range(len(prices)):
            maxTwoTrans = max(maxTwoTrans, dp[i] + dp1[i])

        return maxTwoTrans


testClass = Solution()

print(testClass.maxProfit([2, 1, 2, 0, 1]))
