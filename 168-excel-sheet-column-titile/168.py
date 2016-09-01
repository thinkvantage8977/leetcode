class Solution(object):

    def convertToTitle(self, n):
        res = ""

        while n != 0:
            r = (n - 1) % 26
            res = chr(r + 65) + res
            n = (n - 1) // 26
        return res


testClass = Solution()

print(testClass.convertToTitle(100))
