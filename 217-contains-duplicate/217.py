class Solution(object):

    def containsDuplicate(self, nums):
        numsDict = {}
        for n in nums:
            if n in numsDict:
                return True
            else:
                numsDict[n] = 1
        return False
