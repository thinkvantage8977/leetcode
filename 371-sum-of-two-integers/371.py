class Solution(object):

    def getSum(self, a, b):
        Mod = 0xFFFFFFFF
        Max = 0x7FFFFFFF

        while b != 0:
            a, b = (a ^ b) & Mod, ((a & b) << 1) & Mod
            
        return a if a < Max else ~(a & Max) ^ Max


testClass = Solution()

print(testClass.getSum(-1, 6))
