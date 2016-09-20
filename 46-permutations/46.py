class Solution(object):

    def DFS(self, l, p):
        if l == self.n:
            self.res.append(p[::])
            return

        for i in range(self.n):
            if self.marker[i] == 0:
                p[l] = self.nums[i]
                self.marker[i] = 1
                self.DFS(l + 1, p)
                self.marker[i] = 0

    def permute(self, nums):
        self.marker = [0] * len(nums)
        self.nums = nums
        self.res = []
        self.n = len(nums)
        self.DFS(0, self.marker[::])
        return self.res


testClass = Solution()

print(testClass.permute([1, 2, 3]))
