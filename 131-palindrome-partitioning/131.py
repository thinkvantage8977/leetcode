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
