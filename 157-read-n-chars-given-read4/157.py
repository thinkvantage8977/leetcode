# The read4 API is already defined for you.
# @param buf, a list of characters
# @return an integer
# def read4(buf):


class Solution(object):

    def read(self, buf, n):
        if n == 0:
            return n

        tempbuf = [""] * 4
        r = min(n, read4(tempbuf))
        buf[:r] = tempbuf[:r]
        totaln = r
        n -= r
        while r == 4:
            r = min(read4(tempbuf), n)
            buf[totaln:totaln + r] = tempbuf[:r]
            totaln += r
            n -= r
        return totaln
