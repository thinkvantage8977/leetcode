import math


class Solution(object):
    value = []
    def numSquares(self, n):
        self.value = [n] * (n + 1)

        self.value[0] = 0

        for i in range(1, n + 1):

            cloest = int(math.sqrt(i))

            if cloest**2 == i:
                self.value[i] = 1
            else:
                for j in range(cloest, 0, -1):

                    if self.value[i - j**2] + 1 < self.value[i]:
                        self.value[i] = self.value[i - j**2] + 1
                    if self.value[i] == 2:
                        break

        return self.value[n]


testClass = Solution()

print(testClass.numSquares(12))
