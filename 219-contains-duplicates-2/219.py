class Solution(object):

    def containsNearbyDuplicate(self, nums, k):
        numDict = {}

        if len(nums) <= 1:
            return False

        for i in range(0, len(nums)):
            if nums[i] in numDict:
                if i - numDict[nums[i]] <= k:
                    return True
                else:
                    numDict[nums[i]] = i
            else:
                numDict[nums[i]] = i

        return False


testClass = Solution()

l = [1, 2, 3, 9, 1]


print(testClass.containsNearbyDuplicate(l, 3))
