
class topologicalSort(object):

    def DFS(self, i):
        if self.visit[i] == -1:
            return False
        if self.visit[i] == 1:
            return True

        self.visit[i] = -1

        for d in self.dependencyTable[i]:
            if not self.DFS(d):
                return False

        self.visit[i] = 1
        self.res.append(i)
        return True

    def Sort(self, n, dependencies):
        self.res = []
        self.visit = [0 for i in range(n)]
        self.dependencyTable = [[] for i in range(n)]

        for d in dependencies:
            self.dependencyTable[d[0]].append(d[1])


        for i in range(n):
            if not self.DFS(i):
                return []

        return self.res


testClass = topologicalSort()

p = [[1, 0], [2, 0], [3, 1], [3, 2]]

print(testClass.Sort(4, p))
