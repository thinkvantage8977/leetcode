class Solution(object):

    def isHappy(self, n):
        d = {}

        while n != 1:
            s = str(n)
            result = 0
            for c in s:
                result += (int(c)**2)
            if result in d:
                return False
            else:
                d[result] = True
            n = result
        print(d)
        return True

testClass = Solution()

print(testClass.isHappy(19))
