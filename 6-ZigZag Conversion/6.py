class Solution(object):
    def convert(self, s, numRows):
        result = ""

        if len(s) < numRows or numRows ==1:
        	return s
        	
        step = 2*(numRows -1)
        count= 0
        for base in range(0,numRows):
        	interval = step - 2*base
        	for j in range(base,len(s),step):
        		result = result + s[j]
        		count +=1
        		if interval>0 and interval <step and j + interval < len(s) and count < len(s):
        			result = result + s[j+interval]
        			count +=1
        return result

#Setup testClass
testClass = Solution()

print(testClass.convert("PAYPALISHIRING",4))      