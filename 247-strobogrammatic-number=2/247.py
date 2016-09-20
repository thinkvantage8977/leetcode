class Solution(object):

    def addTwoNumber(self, n):
        if n == 0:
            return [""]
        if n == 1:
            return ["1", "8", "0"]
        PreviousResult = self.addTwoNumber(n - 2)
        result = []
        for i in PreviousResult:
            if n != self.n:
                result.append("0" + i + "0")
            result.append("1" + i + "1")
            result.append("6" + i + "9")
            result.append("9" + i + "6")
            result.append("8" + i + "8")
        return result

    def findStrobogrammatic(self, n):
        self.n = n
        return self.addTwoNumber(n)


testClass = Solution()

print(testClass.findStrobogrammatic(4))
