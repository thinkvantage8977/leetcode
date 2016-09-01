class Solution(object):

    def isPowerOfThree(self, num):
        if num == 0:
            return False
        while num != 1:
            if num % 3 != 0:
                return False
            num //= 3
        return True

testClass = Solution()

print(testClass.isPowerOfThree(81 * 81 * 81))
