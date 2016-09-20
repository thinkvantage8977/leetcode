# Definition for an interval.
class Interval(object):

    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


class Solution(object):

    def merge(self, intervals):
        if not intervals:
            return []
        intervals.sort(key=lambda x: x.start)
        res = []

        for i in intervals:
            if not res:
                res.append(i)
            else:
                if res[-1].end >= i.start:
                    res[-1].end = max(res[-1].end, i.end)
                else:
                    res.append(i)

        return res


testClass = Solution()

res = testClass.merge([Interval(2, 6), Interval(1, 3), Interval(15, 18), Interval(8, 10)])

for r in res:
    print("{} {}".format(r.start, r.end))
