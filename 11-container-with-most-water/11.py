class Solution(object):

    def maxArea(self, height):
        maxV = 0
        for i in range(len(height)):
            for j in range(len(height)):
                maxV = maxV(maxV, min(i[1], j[1]) * abs(i[0] - j[0]))

        return maxV