class Solution(object):

    def wiggleSort(self, nums):
        for i in range(1, len(nums)):
            if (i % 2 == 1 and nums[i] <= nums[i - 1]) or (i % 2 == 0 and nums[i] >= nums[i - 1]):
                nums[i], nums[i - 1] = nums[i - 1], nums[i]


testClass = Solution()

l = [3, 5, 2, 1, 6, 4]
testClass.wiggleSort(l)
print(l )
