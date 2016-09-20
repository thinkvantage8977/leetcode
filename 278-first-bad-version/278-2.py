# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):


class Solution(object):

    def firstBadVersion(self, n):
        if not n:
            return -1
        i = 1
        j = n

        while i < j:
            mid = (i + j) // 2

            if isBadVersion(mid):
                j = mid
            else:
                i = mid + 1

        return j
