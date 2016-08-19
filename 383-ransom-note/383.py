class Solution(object):
	def canConstruct(self, ransomNote, magazine):
		magDict = {}

		for c in magazine:
			if c in magDict:
				magDict[c] += 1
			else:
				magDict[c] = 1

		#print(magDict)

		for c in ransomNote:
			if c in magDict:
				magDict[c] -=1
				if magDict[c] == 0:
					del magDict[c]
			else:
				#print(magDict)
				return False
		return True		

testClase = Solution()


print(testClase.canConstruct("aa","aab"))