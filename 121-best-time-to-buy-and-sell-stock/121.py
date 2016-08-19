class Solution(object):

    def maxProfit(self, prices):
    	if not prices:
    		return 0
        minValue = prices[0]
        maxprofit = 0

        for n in prices:
            if n - minValue > maxprofit:
                maxprofit = n - minValue
            if minValue > n:
                minValue = n

        return maxprofit


testClass = Solution()

l = [7,6,4,3,2,1]


print(testClass.maxProfit(l))
