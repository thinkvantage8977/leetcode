# Definition for an interval.
class Interval(object):

    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


class Solution(object):

    def partition(self, l, left, right):
        pivot = l[(left + right) // 2]
        while left <= right:

            while l[left].start < pivot.start:
                left += 1
            while l[right].start > pivot.start:
                right -= 1

            if left <= right:
                l[left], l[right] = l[right], l[left]
                left += 1
                right -= 1

        return left

    def quickSort(self, l, left, right):
        index = self.partition(l, left, right)
        if left < index - 1:
            self.quickSort(l, left, index - 1)
        if index < right:
            self.quickSort(l, index, right)

    def canAttendMeetings(self, intervals):
        if not intervals:
            return True
        self.quickSort(intervals, 0, len(intervals) - 1)

        for i in range(1, len(intervals)):
            if intervals[i].start < intervals[i - 1].end:
                return False
        return True


l = [Interval(16, 22), Interval(28, 45), Interval(
    3, 9), Interval(46, 50), Interval(13, 14)]

testClass = Solution()

print(testClass.canAttendMeetings(l))
