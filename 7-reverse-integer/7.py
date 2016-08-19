class Solution(object):
	def reverse(self, x):
		flag = 1
		if x<0:
			flag = -1
			result = str(x*-1)
		else:
			result = str(x)

		result = result[::-1]
		intResult = int(result)
		
		if intResult>= 2**31:
			return 0

		return intResult*flag

testClass = Solution()

print(testClass.reverse(-110000))