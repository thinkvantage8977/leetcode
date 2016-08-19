class Solution(object):
	def reverseWords(self, s):
		wordlist = s.split()
		wordlist = wordlist[::-1]
		return " ".join(wordlist)

testClass = Solution()

print(testClass.reverseWords("      abc cdb"))