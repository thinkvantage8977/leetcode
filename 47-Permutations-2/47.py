class Solution(object):

    def DFS(self, l, p):
        if l == self.n:
            self.res.append(p[::])
            return

        for i in range(self.n):
            if self.marker[i] == 0:
                if l in self.numberDict and self.nums[i] in self.numberDict[l]:
                    continue

                if l not in self.numberDict:
                    self.numberDict[l] = [self.nums[i]]
                else:
                    self.numberDict[l].append(self.nums[i])

                p[l] = self.nums[i]
                self.marker[i] = 1
                self.DFS(l + 1, p)
                self.marker[i] = 0
        del self.numberDict[l]

    def permuteUnique(self, nums):
        self.numberDict = {}
        self.marker = [0] * len(nums)
        self.nums = nums
        self.res = []
        self.n = len(nums)
        self.DFS(0, self.marker[::])
        return self.res


testClass = Solution()

print(testClass.permuteUnique([1, 1, 2]))
