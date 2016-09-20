class Solution(object):

    def myPow(self, x, n):
        if n == 0:
            return 1
        if n < 0:
            return 1 / self.myPow(x, -n)
        elif n % 2 == 0:
            result = self.myPow(x, n // 2)
            return result * result
        else:
            return x * self.myPow(x, n - 1)


testClass = Solution()

print(testClass.myPow(29.6, -5))
