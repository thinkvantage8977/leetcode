# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e


class Solution(object):

    def mergeSort(self, l):
        if len(l) <= 1:
            return l
        mid = len(l) // 2
        left = self.mergeSort(l[:mid])
        right = self.mergeSort(l[mid:])
        return self.merge(left, right)

    def merge(self, left, right):
        if not left:
            return right
        if not right:
            return left

        result = [0] * (len(left) + len(right))

        p1 = p2 = 0

        while p1 < len(left) and p2 < len(right):
            if left[p1].start < right[p2].start:
                result[p1 + p2] = left[p1]
                p1 += 1
            else:
                result[p1 + p2] = right[p2]
                p2 += 1

        while p1 < len(left):
            result[p1 + p2] = left[p1]
            p1 += 1

        while p2 < len(right):
            result[p1 + p2] = right[p2]
            p2 += 1
        return result

    def canAttendMeetings(self, intervals):
        l = self.mergeSort(intervals)
        for i in range(1, len(l)):
            if l[i].start < l[i - 1].end:
                return False
        return True
