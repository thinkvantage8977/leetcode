class Solution(object):

    def twoSum(self, nums, target):

        indexDict = {}
        for i in range(len(nums)):
            if i not in indexDict:
                indexDict[nums[i]] = i
            else:
                indexDict[nums[i]].append(i)

        nums.sort()

        res = []

        i = 0
        j = len(nums) - 1

        while i < j:
            if nums[i] + nums[j] == target:
                if nums[i]==nums[j]:
                    return indexDict[nums[i]]
                return [indexDict[nums[i]], indexDict[nums[j]]]
            else:
                if nums[i] + nums[j] < target:
                    i += 1
                else:
                    j -= 1


testClass = Solution()

print(testClass.twoSum([2, 7, 11, 15], 9))
