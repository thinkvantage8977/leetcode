class Solution(object):

    def climbStairs(self, n):
        if n == 1:
            return 1
        if n == 2:
            return 2

        n1 = 1
        n2 = 2
        n3 = 0
        n -= 2
        while n > 0:
            n -= 1
            n3 = n1 + n2
            n1, n2 = n2, n3
        return n3
