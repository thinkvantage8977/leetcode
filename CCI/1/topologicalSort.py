class TopologicalSort(object):

    def __init__(self, n, prerequist):
        self.visit = [0] * n
        self.dependency = [[] for i in range(n)]
        self.n = n
        for p in prerequist:
            self.dependency[p[0]].append(p[1])

    def DFS(self, i):
        if self.visit[i] == -1:
            return False
        if self.visit[i] == 1:
            return True

        self.visit[i] = -1

        for j in self.dependency[i]:
            if not self.DFS(j):
                return False
        self.visit[i] = 1
        self.res.append(i)
        return True

    def sort(self):
        self.res = []
        for i in range(self.n):
            if not self.DFS(i):
                return False
        print(self.res)
        return True
