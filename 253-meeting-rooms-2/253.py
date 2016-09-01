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

    def merge(self, l1, l2):
        res = [0] * (len(l1) + len(l2))
        p1 = 0
        p2 = 0
        while p1 < len(l1) and p2 < len(l2):
            if abs(l1[p1]) < abs(l2[p2]):
                res[p1 + p2] = l1[p1]
                p1 += 1
            elif abs(l1[p1]) > abs(l2[p2]):
                res[p1 + p2] = l2[p2]
                p2 += 1
            elif abs(l1[p1]) == abs(l2[p2]):
                if l1[p1] < 0:
                    res[p1 + p2] = l1[p1]
                    p1 += 1
                else:
                    res[p1 + p2] = l2[p2]
                    p2 += 1

        while p1 < len(l1):
            res[p1 + p2] = l1[p1]
            p1 += 1
        while p2 < len(l2):
            res[p1 + p2] = l2[p2]
            p2 += 1
        return res

    def minMeetingRooms(self, intervals):
        if not intervals:
            return 0

        timeLine = []
        for i in intervals:
            timeLine.append(i.start)
            timeLine.append(-i.end)

        timeLine = self.mergeSort(timeLine)

        maxCount = 0
        count = 0

        for i in timeLine:
            if i > 0:
                count += 1
            if i < 0:
                count -= 1
            maxCount = max(maxCount, count)
        return maxCount
