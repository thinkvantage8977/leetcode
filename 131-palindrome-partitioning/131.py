# 采用了最简单的递归方法，将一个字符串分为前后两部分，如果第一部分是一个回文字符串，
# 则对第二部分再次分割，不断递归，直到递归的终止条件——字符串为空为止；
# 如果第一部分不是一个回文字符串，则尝试下一种分割方法。


class Solution(object):

    def partition(self, s):
        if not s:
            return [[]]
        res = []
        for i in range(len(s)):
            if s[:i + 1] == s[:i + 1][::-1]:
                part = self.partition(s[i + 1:])
                for w in part:
                    res.append([s[:i + 1]] + w)
        return res

    def minCut(self, s):
        res = self.partition(s)
        minl = float("inf")

        for l in res:
            minl = min(len(l), minl)

        return minl - 1


testClass = Solution()

print(testClass.partition("aab"))
