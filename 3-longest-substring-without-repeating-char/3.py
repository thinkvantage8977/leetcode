#Solution Class
class Solution(object):
	def lengthOfLongestSubstring(self, s):
		charDict = {}
		head = 0
		tail = 0
		ans = 0
		while tail< len(s):
			if s[tail] in charDict:
				#The old duplicate one could be behind head, this is very important
				head = max (charDict[s[tail]] + 1, head)
				
				charDict[s[tail]] = tail
			else:
				charDict[s[tail]] = tail
			ans = max(ans,tail - head + 1)
			#print(head,tail,ans)
			
			tail += 1
		#print(charDict , head, tail,len(s))
		return ans





#Setup testClass
testClass = Solution()

print(testClass.lengthOfLongestSubstring("1aba1"))