class Solution(object):
	def multiply(self, num1, num2):
		num1= num1[::-1]
		num2= num2[::-1]

		resultarray = [0 for i in range(len(num1)+len(num2)+ 1)]
		resultarraystr = ["" for i in range(len(num1)+len(num2)+ 1)]

		for i in range(0,len(num1)):
			#print(resultarray)
			for j in range(0,len(num2)):
				resultarray[i+j]+=int(num1[i])*int(num2[j])
				resultarray[i+j+1] += int(resultarray[i+j] / 10)
				resultarray[i+j] = resultarray[i+j] % 10

		result = ""

		for i in range(0,len(resultarray)):
			resultarraystr[i] = str(resultarray[i])

		result =''.join(resultarraystr)[::-1]

		for i in range(0,len(resultarray)):
			if result[i]!= "0":
				return result[i:]

		return "0"


testClass = Solution()


print(testClass.multiply("123123123","456456456"))

