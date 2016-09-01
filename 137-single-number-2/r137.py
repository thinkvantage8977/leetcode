class Solution(object):

    def singleNumber(self, nums):
        one = two = three = 0
        for n in nums:
            two | = (n & one)
            one ^= n
            three = two & one

            two & = ~three
            one & = ~three
