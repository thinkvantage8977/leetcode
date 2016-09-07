from collections import deque


class Solution(object):

    def maxSlidingWindow(self, nums, k):
        d = deque()
        res = []

        for i in range(len(nums)):
            while d and d[0] < i - k + 1:
                d.popleft()

            while d and nums[d[-1]] < nums[i]:
                d.pop()
            d.append(i)

            if d and i >= k - 1:
                res.append(nums[d[0]])

        return res

testClass = Solution()

l = [7, 2, 4]

print(testClass.maxSlidingWindow(l, 2))
