class Solution(object):

    def moveZeroes(self, nums):
        pointer = 0

        for i in range(0, len(nums)):
            if nums[i] != 0:
                nums[pointer] = nums[i]
                pointer += 1

        for i in range(pointer, len(nums)):
            nums[i] = 0


testClass = Solution()

l = [0]


testClass.moveZeroes(l)

print(l)
