class Solution(object):

    def dfs(self, i):
        if i in self.s:
            return
        elif self.visited[i] == 0:
            self.visited[i] = 1
            self.s.append(i)
            for n in self.d[i]:
                self.dfs(n)

    def countComponents(self, n, edges):
        if n == 0:
            return 0

        if not edges:
            return n

        self.visited = [0] * n
        self.d = [[] for i in range(n)]
        c = 0
        for e in edges:
            self.d[e[0]].append(e[1])
            self.d[e[1]].append(e[0])

        for i in range(n):
            self.s = []
            self.dfs(i)
            if self.s:
                c += 1

        return c


n = 5
edges = [[0, 1], [1, 2], [2, 3], [3, 4]]

testClass = Solution()

print(testClass.countComponents(n, edges))
