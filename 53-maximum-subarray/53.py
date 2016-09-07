class Solution(object):

    def maxSubArray(self, nums):
        if not nums:
            return 0

        maxVal = -float("inf")
        sum = 0
        for i in nums:
            if sum > 0:
                sum += i
            else:
                sum = i
            maxVal = max(maxVal, sum)
        return maxVal


        
testClass = Solution()

print(testClass.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
