class Solution(object):
	def isIsomorphic(self, s, t):
		replaceDic = {}

		for i in range(0,len(s)):
			if t[i] in replaceDic:
				if replaceDic[t[i]]!=s[i]:
					print(replaceDic)
					return False
			elif s[i] in replaceDic.values():
				print(replaceDic)
				return False
			else:
				replaceDic[t[i]]=s[i]
		return True


testClass = Solution()

s1= "paperp"
s2= "titleo"

print(testClass.isIsomorphic(s1,s2))