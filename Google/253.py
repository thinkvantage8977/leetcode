# Calculate highest usage


# Definition for an interval.
class Interval(object):

    def __init__(self, s=0, e=0, u=0):
        self.start = s
        self.end = e
        self.usage = u


class Solution(object):

    def minMeetingRooms(self, intervals):

        l = []

        for i in intervals:
            l.append((i.start, i.usage, 1))
            l.append((i.end, i.usage, 2))

        l.sort(key=lambda x: x[0])

        currentUsage = 0
        maxUsage = -float("inf")
        for i in l:
            if i[2] == 1:
                currentUsage += i[1]
                maxUsage = max(maxUsage, currentUsage)
            else:
                currentUsage -= i[1]

        return maxUsage

testClass = Solution()

i = [Interval(0, 3, 15), Interval(5, 9, 10), Interval(2, 8, 30), Interval(23, 45, 100)]


print(testClass.minMeetingRooms(i))
