class Solution(object):

    def maxProfit(self, prices):
        res = 0
        for i in range(1, len(prices)):
            res += prices[i] - prices[i - 1] if prices[i] - prices[i - 1] > 0 else 0
        return res