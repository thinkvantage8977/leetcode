class Solution(object):

    def trailingZeroes(self, n):
        c = 0
        while n:
            n = n // 5
            c += n
        return c
