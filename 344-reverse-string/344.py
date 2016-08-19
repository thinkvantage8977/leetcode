#https://docs.python.org/2/whatsnew/2.3.html#extended-slices
class Solution(object):
    def reverseString(self, s):
        return s[::-1]


 #Setup testClass
testClass = Solution()


#Run
result = testClass.reverseString("1234344234213432")

#Print
print (result)