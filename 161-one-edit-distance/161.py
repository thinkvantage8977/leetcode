class Solution(object):
	def minDistance(self, word1, word2):
		if abs(len(word1)-len(word2)) > 1:
			return False

		if len(word1) == len(word2):
			oneChance= False
			for i in range(0,len(word1)):
				if word1[i]!=word2[i]:
					if oneChance:
						return False
					else:
						oneChance = True
			return True

		if len(word1)>len(word2):
			return self.insert(word1,word2)

	def insert(self,s1,s2):
		i1 = 0
		i2 = 0
		while i1<len(s1):
			if s1[i1]!=s2[i2]:
				if i1==i2:
					i2 + =1
				else:
					return False
			else:
				i1+=1
				i2+=1

		return True



		