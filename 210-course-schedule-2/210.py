class Solution(object):

    def findOrder(self, numCourses, prerequisites):
        depend = [[] for i in range(numCourses)]
        visit = [0] * numCourses
        res = []
        for p in prerequisites:
            depend[p[0]].append(p[1])

        def DFS(i):
            if visit[i] == -1:
                return False
            if visit[i] == 1:
                return True

            visit[i] = -1
            for n in depend[i]:
                if not DFS(n):
                    return False

            res.append(i)
            visit[i] = 1
            return True

        for i in range(numCourses):
            if not DFS(i):
                return []
        return res

testClass = Solution()

print(testClass.findOrder(2, [0, 1]))
