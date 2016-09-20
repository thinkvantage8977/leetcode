# sell[i]表示第i天卖掉股票的最大收益,sell[i]>=sell[i-1]
# buy[i]表示第i天买了股票后的最大收益
# 有如下公式：

# buy[i] = max(buy[i-1], sell[i-2]-prices[i]);
# sell[i] = max(buy[i-1]+prices[i], sell[i-1]);


class Solution(object):

    def maxProfit(self, prices):
        if not prices or len(prices) < 2:
            return 0

        sell = [0] * len(prices)
        buy = [0] * len(prices)

        #初始化 s[0]=0, s[1] = max(0, prices[1] - prices[0]) -> 如果第二天可以赚的话
        sell[0] = 0
        sell[1] = max(0, prices[1] - prices[0])
        #buy[0] = -prices[0], buy[1] = -prices[0] or -prices[1] 买哪天的亏得最少
        buy[0] = -prices[0]
        buy[1] = max(-prices[0], -prices[1])

        for i in range(2, len(prices)):
            buy[i] = max(buy[i - 1], sell[i - 2] - prices[i])
            sell[i] = max(sell[i - 1], buy[i - 1] + prices[i])

        return sell[-1]
