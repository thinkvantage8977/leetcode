class Solution(object):

    def DFS(self, l, left, right):
        if left == right == self.n:
            self.solutions.append("".join(l))
            return
        if left < self.n:
            l.append("(")
            self.DFS(l, left + 1, right)
            l.pop()

        if left > right and right < self.n:
            l.append(")")
            self.DFS(l, left, right + 1)
            l.pop()

    def generateParenthesis(self, n):
        self.solutions = []
        self.n = n
        self.DFS([], 0, 0)

        return self.solutions


testClass = Solution()

print(testClass.generateParenthesis(3))
