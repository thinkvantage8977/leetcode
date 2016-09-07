class Solution(object):

    def canFinish(self, numCourses, prerequisites):
        depend = [[]for i in range(numCourses)]
        marker = [0] * numCourses
        for i in prerequisites:
            depend[i[0]].append(i[1])

        def DFS(n):
            if marker[n] == -1:
                return False
            if marker[n] == 1:
                return True

            marker[n] = -1
            for i in depend[n]:
                if not DFS(i):
                    return False
            marker[n] = 1
            return True

        for i in range(numCourses):
            if not DFS(i):
                return False
        return True


testClass = Solution()

p = [[0, 1]]

print(testClass.canFinish(4, p))
