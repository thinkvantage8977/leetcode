class Solution(object):

    def largestDivisibleSubset(self, nums):
    	if not nums:
    		return []
        nums.sort()
        l = []
        for i in nums:
            l.append([i])

        l[0] = [nums[0]]

        maxLen = 1
        res = l[0]

        for i in range(1, len(nums)):
            for j in range(0, i):
                if nums[i] % nums[j] == 0 and len(l[j]) + 1 > len(l[i]):
                    l[i] = l[j] + [nums[i]]
            if len(l[i]) > maxLen:
                maxLen = len(l[i])
                res = l[i]
        return res


testClass = Solution()

print(testClass.largestDivisibleSubset([1, 2, 4,8,3]))
