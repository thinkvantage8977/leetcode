class Solution(object):

    def rob(self, nums):
        if not nums:
            return 0
        if len(nums) <= 2:
            return max(nums)
            
        dp = [0] * len(nums)

        dp[0] = nums[0]
        dp[1] = nums[0]

        for i in range(2, len(nums)):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])

        r1 = dp[-2]

        dp[0] = 0
        dp[1] = nums[1]

        for i in range(2, len(nums)):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])

        r2 = dp[-1]

        return max(r1, r2)
