class Solution(object):

    def isPowerOfFour(self, num):

        a = 0b010101010101010101010101010101010101

        return num > 0 and num & (num - 1) == 0 and num & a != 0


testClass = Solution()

print(testClass.isPowerOfFour(5))
print(testClass.isPowerOfFour(4))
print(testClass.isPowerOfFour(16))
print(testClass.isPowerOfFour(64))
print(testClass.isPowerOfFour(12))
print(testClass.isPowerOfFour(1024))
