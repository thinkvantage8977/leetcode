class Solution(object):

    def jump(self, nums):
        jumpCounter = 0
        currentMax = 0
        lastMax = 0
        for i in range(len(nums)):
            if lastMax < i:
                lastMax = currentMax
                jumpCounter += 1
            currentMax = max(currentMax, i + nums[i])
        
        return jumpCounter


testClass = Solution()

print(testClass.jump([2, 3, 1, 1, 4]))
