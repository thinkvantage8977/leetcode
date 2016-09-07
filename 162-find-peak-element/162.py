class Solution(object):

    def findPeakElement(self, nums):
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = (left + right) // 2

            midr = mid + 1

            if nums[mid] < nums[midr]:
                left = midr
            else:
                right = mid

        return left
