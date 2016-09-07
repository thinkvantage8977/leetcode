class Solution(object):

    def numWays(self, n, k):
        if n == 0:
            return 0
        if n == 1:
            return k
        if n == 2:
            return k**2

        f1 = k
        f2 = k**2
        f3 = 0

        n -= 2
        while n > 0:
            f3 = f1 * (k - 1) + f2 * (k - 1)
            n -= 1
            f1, f2 = f2, f3

        return f3
