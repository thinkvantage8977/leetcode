class Solution(object):

    def mySqrt(self, x):
        left = 1
        right = x
        if x == 0:
            return 0

        while True:
            mid = (left + right) // 2
            if mid * mid > x:
                right = mid - 1
            else:
                if (mid + 1) * (mid + 1) > x:
                    return mid
                left = mid + 1


testClass = Solution()

print(testClass.mySqrt(6))
