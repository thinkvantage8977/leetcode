class Solution(object):

    def countNumbersWithUniqueDigits(self, n):
        if n == 0:
        	return 1
        total = 10
        if n == 1:
            return total

        for i in range(2, n + 1):
            s = 9
            for j in range(2, i + 1):
                s *= (9 - j + 2)
            total += s
        return total

testClass = Solution()

print(testClass.countNumbersWithUniqueDigits(3))
