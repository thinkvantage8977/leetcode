class Solution(object):

    def minCost(self, costs):
        price = []
        if not costs:
            return 0
        price.append(costs[0][::])

        for i in range(1, len(costs)):
            price.append([min(price[i - 1][1], price[i - 1][2]) + costs[i][0], min(price[i - 1][0], price[i - 1][2]) + costs[i][1], min(price[i - 1][0], price[i - 1][1]) + costs[i][2]])
        print(price)
        return min(price[len(costs) - 1])


testClass = Solution()
l = [[3, 5, 3], [6, 17, 6], [7, 13, 18], [9, 10, 18]]
print(testClass.minCost(l))
