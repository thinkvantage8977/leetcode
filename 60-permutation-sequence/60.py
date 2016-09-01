class Solution(object):

    def DFS(self, l, s):
        if self.count == self.k:
            return
        if l == self.n:
            self.count += 1
            self.current = "".join(s)
            return

        for i in range(0, self.n):
            if self.marker[i] == 0:
                self.marker[i] = 1
                s.append(str(i + 1))
                self.DFS(l + 1, s)
                s.pop()
                self.marker[i] = 0

    def getPermutation(self, n, k):
        self.count = 0
        self.current = ""
        self.marker = [0] * n
        self.k = k
        self.n = n
        self.DFS(0, [])
        return self.current


testClass = Solution()

print(testClass.getPermutation(1, 1))
