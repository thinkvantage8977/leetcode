import math


class Solution(object):

    def countPrimes(self, n):
        if n ==0 or n == 1:
            return 0
        table = [True] * (n + 1)
        table[0] = False
        table[1] = False
        for i in range(n):
            if table[i]:
                factor = i * i
                while factor <= n:
                    table[factor] = False
                    factor += i

        count = 0
        for i in range(n):
            if table[i]:
                count += 1
        return count

testClass = Solution()

print(testClass.countPrimes(0))
