class Solution(object):

    def trace(self, i):

        if self.parents[i] != -1:
            return 1 + self.parents[i]

        if self.nums[i] - 1 in self.s:
            self.parents[i] = 1 + self.trace(self.s[self.nums[i] - 1])
            return self.parents[i]
        else:
            self.parents[i] = 1
            return 1

    def longestConsecutive(self, nums):
        if not nums:
            return 0

        self.s = {}

        for i in range(len(nums)):
            self.s[nums[i]] = i

        self.nums = nums
        self.parents = [-1] * len(nums)

        for i in range(len(nums)):
            if self.parents[i] == -1:
                self.parents[i] = self.trace(i)
                print(self.parents)

        return max(self.parents)


testClass = Solution()

print(testClass.longestConsecutive([100, 4, 200, 1, 3, 2]))
