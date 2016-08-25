class Solution(object):

    def findRepeatedDnaSequences(self, s):
        strDict = {}
        result = []
        for i in range(0, len(s) - 9):
            if s[i:i + 10] in strDict:
                strDict[s[i:i + 10]] += 1
            else:
                strDict[s[i:i + 10]] = 1
        # print(strDict)
        for key, value in strDict.items():
            if value > 1:
                result.append(key)
        return result

testClass = Solution()


s = "AAAAAAAAAAA"


print(testClass.findRepeatedDnaSequences(s))
