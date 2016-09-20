class Solution(object):

    def DFS(self, numberofLeft, l, currentS):

        if l == len(self.s):
            if numberofLeft == 0:
                if len(currentS) >= self.maxl:
                    self.res.append(currentS)
                    self.maxl = max(self.maxl, len(currentS))
            return
        else:
            if self.s[l] == ")" and numberofLeft > 0:
                print(currentS)
                self.DFS(numberofLeft - 1, l + 1, currentS + ")")
                self.DFS(numberofLeft, l + 1, currentS)
            elif self.s[l] == "(":
                self.DFS(numberofLeft + 1, l + 1, currentS + "(")
                self.DFS(numberofLeft, l + 1, currentS)
            else:
                self.DFS(numberofLeft, l + 1, currentS + self.s[l])

    def removeInvalidParentheses(self, s):
        self.s = s
        self.maxl = 0 
        self.res = []
        self.DFS(0, 0, "")
       

        return self.res


testClass = Solution()

print(testClass.removeInvalidParentheses("()())()"))
