class Solution(object):

    def DFS(self, i, s):
        if i == self.digitsLen:
            self.result.append(s)
            return
        for j in self.numLetter[int(self.digits[i])]:
            self.DFS(i + 1, s + j)

    def letterCombinations(self, digits):
        if not digits:
            return []
        self.numLetter = {1: [''], 2: ['a', 'b', 'c'], 3: ['d', 'e', 'f'], 4: ['g', 'h', 'i'], 5: [
            'j', 'k', 'l'], 6: ['m', 'n', 'o'], 7: ['p', 'q', 'r', 's'], 8: ['t', 'u', 'v'], 9: ['w', 'x', 'y', 'z']}
        self.digits = digits
        self.digitsLen = len(digits)
        self.result = []
        self.DFS(0, "")
        return self.result


testClass = Solution()

print(testClass.letterCombinations("23"))
