class topologicalSort(object):

    def __init__(self, n, prerequist):
        self.visit = [0] * len(l)
        self.depend = [[]for i in range(n)]
        self.n = n
        for p in prerequist:
            self.depend[p[0]].append(p[1])

    def DFS(self, i):
        if self.visit[i] == -1:
            return False
        if self.visit[i] == 1:
            return True

        self.visit[i] = -1
        for d in self.depend[i]:
            if not self.DFS(d):
                return False
        self.visit[i] = 1
        self.res.append(i)
        return True

    def Sort(self):
        self.res = []
        for i in range(self.n):
            if not self.DFS(i):
                return []
        return self.res
