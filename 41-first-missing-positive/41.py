class Solution(object):

    def firstMissingPositive(self, nums):

        n = len(nums)
        
        i = 0
        while i < n:
            if nums[i] == i + 1 or nums[nums[i] - 1] == nums[i] or nums[i] <= 0 or nums[i] > n:
                i += 1
            else:
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]

        for i in range(n):
            if nums[i] != i + 1:
                return i + 1

        return n+1

testClass = Solution()

print(testClass.firstMissingPositive([3]))
