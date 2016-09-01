class Solution(object):

    def nthUglyNumber(self, n):
        p2 = p3 = p5 = 0
        l = [0] * n
        l[0] = 1

        for i in range(1, n):
            t2 = l[p2] * 2
            t3 = l[p3] * 3
            t5 = l[p5] * 5
            l[i] = min(t2, min(t3, t5))

            if l[i] == t2:
                p2 += 1
            if l[i] == t3:
                p3 += 1
            if l[i] == t5:
                p5 += 1

        return l[n - 1]

testClass = Solution()
print(testClass.nthUglyNumber(10))
