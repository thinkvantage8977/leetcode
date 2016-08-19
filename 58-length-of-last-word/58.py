class Solution(object):
	def lengthOfLastWord(self, s):
		l = s.split()
		if len(l)==0:
			return 0
		print(l)
		return len(l[-1])


testClass= Solution()

print(testClass.lengthOfLastWord("a "))