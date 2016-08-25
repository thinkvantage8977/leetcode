class Solution(object):

    def reverseBits(self, n):

        s = str(bin(n))[2:][::-1]

        while len(s) != 32:
            s = s + "0"

        return int(s, 2)

testClass = Solution()

print(testClass.reverseBits(43261596))
