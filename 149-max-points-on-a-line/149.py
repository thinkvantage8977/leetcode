# Definition for a point.
# class Point(object):
#     def __init__(self, a=0, b=0):
#         self.x = a
#         self.y = b


class Solution(object):

    def maxPoints(self, points):
    	if not points:
    		return 0
        x = {}
        y = {}
        maxpoint = 1
        for p in points:
            if p.x in x:
                x[p.x].append(p.y)
                maxpoint = max(maxpoint, len(x[p.x]))
            else:
                x[p.x] = [p.y]

            if p.y in y:
                y[p.y].append(p.x)
                maxpoint = max(maxpoint, len(y[p.y]))
            else:
                y[p.y] = [p.x]

        return maxpoint
