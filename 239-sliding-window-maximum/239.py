
# Given nums = [1,3,-1,-3,5,3,6,7], and k = 3.
# 用一个linkedlist保存进入窗口的数的index.
# 如果3出现, 则1没有可能是最大值. 所以可以移除1. 然后-1出现.
# 这个时候不能移除3. 因为 3可能是最大值.  也就是说如果后出现的数比先出现的数要大,
# 则可以删除之前的数. 当list顶部的index超出窗口时,则移除.   这样list中的数应该是降序排列, 分别是
# [最大的数, 第2大的数, 第3大的数, ....]

from collections import deque


class Solution(object):

    def maxSlidingWindow(self, nums, k):
        d = deque()
        res = []

        for i in range(len(nums)):
            # if the left top is out of the index , popleft
            while d and d[0] < i - k + 1:
                d.popleft()

            # if the current pop is smaller than the new, it will never be the max, pop it
            while d and nums[d[-1]] < nums[i]:
                d.pop()

            d.append(i)

            # put the left top to res
            if d and i >= k - 1:
                res.append(nums[d[0]])

        return res

testClass = Solution()

l = [7, 2, 4]

print(testClass.maxSlidingWindow(l, 2))
