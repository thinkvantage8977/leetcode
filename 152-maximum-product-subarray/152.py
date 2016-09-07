class Solution(object):

    def maxProduct(self, nums):
        dp1 = [1] * len(nums)
        dp2 = [1] * len(nums)

        dp1[0] = nums[0]
        dp2[0] = nums[0]

        for i in range(1, len(nums)):
            if nums[i] == 0:
                dp1[i] = 0
                dp2[i] = 0
            else:
                dp1[i] = max(dp1[i-1]*nums[i],dp2[i-1]*nums[i],nums[i])
                dp2[i] = min(dp1[i-1]*nums[i],dp2[i-1]*nums[i],nums[i])


        max1 = max(dp1)
        max2 = max(dp2)

        return max(max1, max2)


testClass = Solution()


print(testClass.maxProduct([2, -5,-2,-4,3]))
