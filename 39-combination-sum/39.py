class Solution(object):

    def DFS(self, l, i, current):
        print(l)
        if current == self.target:
            self.result.append(l[:])
            return

        if i == self.n:
            return

        for j in range(i, self.n):
            if current + self.candidates[j] <= self.target:
                l.append(self.candidates[j])
                self.DFS(l, i + 1, current + self.candidates[j])
                l.pop()

    def combinationSum(self, candidates, target):
        self.n = len(candidates)
        self.result = []
        self.candidates = candidates
        self.target = target
        self.DFS([], 0, 0)
        return self.result

testClass = Solution()

print(testClass.combinationSum([2, 3, 6, 7], 7))
