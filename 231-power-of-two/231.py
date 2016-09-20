#如果是power of two, 则2进制表达中,有且仅有一个1.  
#可以通过移位来数1的个数, 这里用了一个巧妙的办法, 即判断   N & (N-1) 是否为0. 
class Solution(object):

    def isPowerOfTwo(self, n):

        return n > 0 and n & (n - 1) == 0
