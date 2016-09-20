# Definition for an interval.
class Interval(object):

    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


class Solution(object):

    def minMeetingRooms(self, intervals):
        newL = []
        for i in intervals:
            newL.append(i.start)
            newL.append(i.end * -1)
        newL = sorted(newL, key=lambda x: abs(x))

        r = 0
        res = 0
        for i in newL:
            if i >= 0:
                r += 1
                res = max(res, r)
            else:
                r -= 1
        return res


testClass = Solution()

i = [Interval(0, 30), Interval(5, 10), Interval(15, 20)]

print(testClass.minMeetingRooms(i))
