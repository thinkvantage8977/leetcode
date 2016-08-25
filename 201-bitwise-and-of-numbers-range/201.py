class Solution(object):

    def rangeBitwiseAnd(self, m, n):
        shitfCounter = 0

        while m != n:
            m >>= 1
            n >>= 1
            shitfCounter += 1
        return m << shitfCounter

