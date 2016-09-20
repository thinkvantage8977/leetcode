class Solution(object):

    def DFS(self, n, s):
        if n >= self.l:
            self.res.append(s)
            return
        else:
            if self.digits[n] in "01":
                self.DFS(n + 1, s)
            else:
                for i in self.d[self.digits[n]]:
                    self.DFS(n + 1, s + i)

    def letterCombinations(self, digits):
        if not digits:
            return []

        self.l = len(digits)
        self.digits = digits
        self.d = {"1": "", "2": "abc", "3": "def",
                  "4": "ghi", "5": "jkl", "6": "mno",
                  "7": "pqrs", "8": "tuv", "9": "wxyz", "0": ""}
        self.res = []
        self.DFS(0, "")

        return self.res


testClass = Solution()

print(testClass.letterCombinations("1230"))
