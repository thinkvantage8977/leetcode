class Solution(object):
    def addBinary(self, a, b):
        a = a[::-1]
        b = b[::-1]

        resultarray = [0 for i in range(len(a)+len(b)+ 1)]
        
        for i in range(0,len(a)):
        	resultarray[i]= int(a[i])

        for i in range(0,len(b)):
        	resultarray[i] = resultarray[i] + int(b[i])

        for i in range(0,len(resultarray)):
        	if resultarray[i] == 2:
        		resultarray[i] = 0
        		resultarray[i+1] +=1
        	if resultarray[i] == 3:
        		resultarray[i] = 1
        		resultarray[i+1] +=1

        resultarray=  resultarray[::-1]

        for i in range(0,len(resultarray)):
        	if resultarray[i]==1:
        		resultarray = resultarray[i:]
        		return ''.join(str(x) for x in resultarray)
        return '0'


testClass = Solution()

print(testClass.addBinary('0','0'))



