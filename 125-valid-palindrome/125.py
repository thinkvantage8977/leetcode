class Solution(object):
	def isPalindrome(self, s):
		
		targetstrings= "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
		newstr= []
		l = len(s)
		for c in s:
			if c in targetstrings:
				newstr.append(c)

		news = "".join(x.lower() for x in newstr)

		print(news)

		l = len(news)

		i = 0

		while i< (l/2):
			if news[i]!=news[l-i-1]:
				return False
			i+=1

		return True


testClass= Solution()

print(testClass.isPalindrome("0P"))	
			