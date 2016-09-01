class Solution(object):

    def addDigits(self, num):

        while len(str(num)) != 1:
            a = 0
            for i in str(num):
                a += int(i)
            num = a
        return num

testClass= Solution()

print(testClass.addDigits(38))