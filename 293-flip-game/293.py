class Solution(object):

    def generatePossibleNextMoves(self, s):
        res = []
        for i in range(0,len(s)-1):
        	if s[i:i+2] == "++":
        		res.append(s[:i]+"--"+s[i+2:])
        return res

testClass = Solution()

print(testClass.generatePossibleNextMoves("++++"))
