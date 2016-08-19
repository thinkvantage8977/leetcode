class Solution(object):
    def wordPattern(self, pattern, str):
        wordlist = str.split(" ")
        if len(wordlist)!=len(pattern):
        	return False

        patternDict = {}

        for i in range(0,len(pattern)):
        	if wordlist[i] in patternDict:
        		if patternDict[wordlist[i]]!=pattern[i]:
        			return False
        	elif pattern[i] in patternDict.values():
        		return False
        	else:
        		patternDict[wordlist[i]]=pattern[i]

        return True




testClass = Solution()

print(testClass.wordPattern("abba","dog cat cat fish"))