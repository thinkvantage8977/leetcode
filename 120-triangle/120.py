class Solution(object):

    def minimumTotal(self, triangle):
    	if not triangle:
    		return 0
        for l in range(1, len(triangle)):
            triangle[l][0] += triangle[l - 1][0]
            triangle[l][-1] += triangle[l - 1][-1]
            for i in range(1, len(triangle[l]) - 1):
                triangle[l][i] += min(triangle[l - 1][i], triangle[l - 1][i - 1])

        return min(triangle[-1])
