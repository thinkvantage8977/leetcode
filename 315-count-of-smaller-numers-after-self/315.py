
import bisect


class Solution(object):

    def countSmaller(self, nums):
        sortedArray = []
        res = []
        for i in range(len(nums) - 1, -1, -1):
            res.append(bisect.bisect_left(sortedArray, nums[i]))
            bisect.insort(sortedArray, nums[i])
        return res[::-1]


testClass = Solution()

print(testClass.countSmaller([5, 2, 6, 1]))
