class Solution(object):

    def titleToNumber(self, s):
        s = s[::-1]
        res = 0

        for i in range(len(s)):
        	res += (ord(s[i]) -64) * (26**i)
        return res


testClass = Solution()

print(testClass.titleToNumber("CV"))
