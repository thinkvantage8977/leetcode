class Solution(object):

    def DFS(self, l, current, n):
        if current == 0:
            self.result.append(l)
            return

        for i in range(n, len(self.candidates)):
            if current - self.candidates[i] < 0:
                return

            self.DFS(l + [self.candidates[i]], current - self.candidates[i], i)

    def combinationSum(self, candidates, target):
        self.result = []
        self.candidates = candidates
        self.candidates.sort()
        self.DFS([], target, 0)
        return self.result

testClass = Solution()

print(testClass.combinationSum([2, 3, 6, 7], 7))
