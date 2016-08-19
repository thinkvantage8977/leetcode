class Solution(object):
	
	def compress(self,s):
		result = []
		i = 0
		count = 1
		current = s[i]
		while i < len(s)-1:
			if s[i+1]!=s[i]:
				result.append(str(count))
				result.append(str(s[i]))
				count = 1
				current = s[i+1]
			else:
				count +=1
			i +=1
		result.append(str(count))
		result.append(str(s[i]))
		return "".join(result)


	def countAndSay(self, n):
		
		result = "1"

		for i in range(0,n-1):
			result = self.compress(result)
			#print(result)
		return result


testClass = Solution()

print(testClass.countAndSay(1))