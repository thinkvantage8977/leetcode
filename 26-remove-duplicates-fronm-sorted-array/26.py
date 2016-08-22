class Solution(object):

    def removeDuplicates(self, nums):
        if not nums:
            return 0
        current = nums[0]
        pointer = 0

        for i in range(0, len(nums)):
            if nums[i] != current:
                pointer += 1
                nums[pointer] = current = nums[i]

        return pointer + 1


testClass = Solution()

l = [1, 1, 1, 1]

print(testClass.removeDuplicates(l))
print(l)
