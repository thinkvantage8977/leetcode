class Solution(object):

    def combinationSum4(self, nums, target):
        dp = [0] * (target + 1)
        for i in nums:
            if i <= target:
                dp[i] = 1

        for i in range(1, target + 1):
            for j in nums:
                if (i - j) >= 0:
                    dp[i] += dp[i - j]
        return dp[target]


testClass = Solution()

nums = [3,4,5,6,7,8,9,10]
print(testClass.combinationSum4(nums, 10))
