class Solution(object):

    def nextPermutation(self, nums):
        if not nums:
            return nums

        i = len(nums) - 2

        while i > 0:
            if nums[i] < nums[i + 1]:
                break
            else:
                i -= 1

        if i == 0:
            return sorted(nums)

        j = len(nums) - 1

        while nums[j] < nums[i]:
            j -= 1

        nums[i], nums[j] = nums[j], nums[i]

        nums[i + 1:] = sorted(nums[i + 1:])

        return nums

testClass = Solution()

print(testClass.nextPermutation([1, 2, 3]))
print(testClass.nextPermutation([1, 1, 5]))
print(testClass.nextPermutation([6, 5, 4, 8, 7, 5, 1]))
# print(testClass.nextPermutation[1, 2, 3])
