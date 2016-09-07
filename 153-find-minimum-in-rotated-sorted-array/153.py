class Solution(object):

    def findMin(self, nums):
        left = 0
        right = len(nums) - 1

        while left < right:
            mid = (left + right) // 2

            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid

        return nums[left]


testClass = Solution()

print(testClass.findMin([4, 5, 6, 7, 0, 1, 2]))
