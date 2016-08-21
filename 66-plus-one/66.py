class Solution(object):

    def plusOne(self, digits):
        digits = digits[::-1]
        digits[0]+=1

        for i in range(0,len(digits)-1):
        	if digits[i]>9:
        		digits[i] -=10
        		digits[i+1] +=1

        if digits[len(digits)-1] >9:
        	digits[len(digits)-1] -=10
        	digits.extend([1])

        return digits[::-1]



testClass= Solution()
digits = [9,9,9,9,9]

print(testClass.plusOne(digits))
