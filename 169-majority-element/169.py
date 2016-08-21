class Solution(object):

    def majorityElement(self, nums):
        dictNums = {}

        for n in nums:
            if n in dictNums:
                dictNums[n] += 1
            else:
                dictNums[n] = 1
            
            if dictNums[n] > (len(nums) / 2):
                return n

        return None


testClass = Solution()

l = [1]

print(testClass.majorityElement(l))
