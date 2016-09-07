class Solution(object):

    def lengthOfLIS(self, nums):
        if not nums:
            return 0
        dp = [1] * (len(nums))
        res = 1
        for i in range(1, len(nums)):
            for j in range(0, i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
                    res = max(dp[i], res)

        return res


testClass = Solution()

l = [10, 9, 2, 5, 3, 7, 101, 18]

print(testClass.lengthOfLIS(l))
