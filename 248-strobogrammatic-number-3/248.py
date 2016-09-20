class Solution(object):

    def addTwo(self, n, m):
        if n == 0:
            return [""]
        if n == 1:
            return ["1", "0", "8"]
        p = self.addTwo(n - 2, m)
        res = []
        for i in p:
            if n != m:
                res.append("0" + i + "0")
            res.append("1" + i + "1")
            res.append("6" + i + "9")
            res.append("8" + i + "8")
            res.append("9" + i + "6")
        return res

    def strobogrammaticInRange(self, low, high):

        total = []

        for i in range(len(low), len(high) + 1):
            total += self.addTwo(i, i)

        count = 0

        for p in total:
            if long(low) <= long(p) <= long(high):
                count += 1
        return count


testClass = Solution()

print(testClass.strobogrammaticInRange("50", "100"))
