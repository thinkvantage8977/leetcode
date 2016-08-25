import math


class Solution(object):

    def bulbSwitch(self, n):
        return int(math.sqrt(n))


testClass = Solution()

print(testClass.bulbSwitch(9))
