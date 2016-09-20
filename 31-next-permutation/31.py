class Solution(object):

    def nextPermutation(self, nums):
        i = len(nums) - 2

        while nums[i] >= nums[i + 1] and i >= 0:
            i -= 1

        if i < 0:
            nums.sort()
            return

        j = len(nums) - 1

        while nums[j] <= nums[i] and j > i:
            j -= 1

        nums[i], nums[j] = nums[j], nums[i]

        nums[i + 1:] = sorted(nums[i + 1:])


testClass = Solution()


l = [1, 2, 3]

testClass.nextPermutation(l)

print(l)
