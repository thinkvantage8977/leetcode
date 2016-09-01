import math


class Solution(object):

    def isPrime(self, n):
        r = int(math.sqrt(n))
        for i in range(2, r + 1):
            if n % i == 0:
                return False
        # print(n)
        return True

    def countPrimes(self, n):
        count = 0
        for i in range(2, n):
            if self.isPrime(i):
                count += 1
        return count


testClass = Solution()

print(testClass.countPrimes(2))
