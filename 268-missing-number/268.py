class Solution(object):

    def missingNumber(self, nums):
        end = len(nums) + 1
        targetSum = (end * (end - 1)) / 2
        for n in nums:
            targetSum -= n
        return int(abs(targetSum))


testClass = Solution()

l=[1,2,3,4,5,6,7]

print(testClass.missingNumber(l))
