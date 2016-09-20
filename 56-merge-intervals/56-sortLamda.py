# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution(object):
    def merge(self, intervals):
        intervals = sorted(intervals,key=lambda interval: interval.start)

        for i in intervals:
            print("{},{}".format(i.start, i.end))

        ans = [intervals[0]]
        #对区间集合按照 start 来排序，然后根据 intervals[i].start 和 res.lastElement.end 来整合即可。
        for i in range(0, len(intervals)):
            top = ans.pop()
            if top.end >= intervals[i].start:
                ans.append(Interval(top.start, max(intervals[i].end, top.end)))
            else:
                ans.append(top)
                ans.append(intervals[i])
        return ans
        

testClass=Solution()

l=[Interval(1, 3), Interval(8, 10),Interval(15, 18),Interval(2, 6),]


ans=testClass.merge(l)

for i in ans:
    print("{},{}".format(i.start, i.end))
