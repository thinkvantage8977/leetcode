class Solution(object):

    def singleNumber(self, nums):
        one = two = three = 0

        for n in nums:
            # number that appers exactly twice
            two = two | (one & n)
            # number that appears exactly once
            one = one ^ n
            # number that appears exactly three times
            three = one & two
            one = one & (~ three)
            two = two & (~ three)
        return one


testClass = Solution()

nums = [1, 1, 1, 2, 2, 2, 3]

print(testClass.singleNumber(nums))
