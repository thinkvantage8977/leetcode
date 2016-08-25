class Solution(object):

    def singleNumber(self, nums):
        result = [0, 0]
        twoNumbs = 0
        for n in nums:
            twoNumbs ^= n

        first1 = twoNumbs & (-twoNumbs)
        for n in nums:
            if n & first1 == 0:
                result[0] ^= n
            else:
                result[1] ^= n
        return result

testClass = Solution()
nums = [1, 2, 1, 3, 2, 5]

print(testClass.singleNumber(nums))
