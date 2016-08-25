class Solution(object):

    def countBits(self, num):
        result = [0] * (num + 1)

        for i in range(0, num + 1):
            result[i] = result[i >> 1] + (i & 1)

        return result


testClass = Solution()

print(testClass.countBits(5))
