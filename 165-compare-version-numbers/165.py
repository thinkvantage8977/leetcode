class Solution(object):
	def compareVersion(self, version1, version2):

		a1 = version1.split(".")
		a2 = version2.split(".")

		l = max(len(a1),len(a2))

		for i in range(0,l):

			if i < len(a1):
				num1 = int(a1[i])
			else:
				num1 = 0

			if i< len(a2):
				num2 = int(a2[i])
			else:
				num2 = 0

			if num1<num2:
				return -1
			elif num1>num2:
				return 1

		return 0

testClass = Solution()

print(testClass.compareVersion("0001.3.2","1.3.1.1"))