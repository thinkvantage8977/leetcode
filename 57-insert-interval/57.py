# Definition for an interval.
class Interval(object):

    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


class Solution(object):

    def mergeSortHelper(self, l1, l2):
        ans = [None] * (len(l1) + len(l2))
        p1 = 0
        p2 = 0
        while p1 < len(l1) and p2 < len(l2):
            if l1[p1].start < l2[p2].start:
                ans[p1 + p2] = l1[p1]
                p1 += 1
            elif l1[p1].start == l2[p2].start and l1[p1].end < l2[p2].end:
                ans[p1 + p2] = l1[p1]
                p1 += 1
            else:
                ans[p1 + p2] = l2[p2]
                p2 += 1
        while p1 < len(l1):
            ans[p1 + p2] = l1[p1]
            p1 += 1
        while p2 < len(l2):
            ans[p1 + p2] = l2[p2]
            p2 += 1

        return ans

    def mergeSort(self, l):
        if len(l) <= 1:
            return l

        mid = (0 + len(l)) // 2

        left = self.mergeSort(l[:mid])
        right = self.mergeSort(l[mid:])

        return self.mergeSortHelper(left, right)

    def merge(self, intervals):
        if not intervals:
            return intervals
        intervals = self.mergeSort(intervals)
        
        ans = [intervals[0]]
        for i in range(0, len(intervals)):
            top = ans.pop()
            if top.end >= intervals[i].start:
                ans.append(Interval(top.start, max(intervals[i].end, top.end)))
            else:
                ans.append(top)
                ans.append(intervals[i])
        return ans

    def insert(self, intervals, newInterval):
        return self.merge(intervals + [newInterval])

testClass = Solution()

l = [Interval(1, 3), Interval(6, 9)]
l2 = Interval(2, 5)


ans = testClass.insert(l, l2)

for i in ans:
    print("{},{}".format(i.start, i.end))
