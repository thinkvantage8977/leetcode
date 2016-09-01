class Solution(object):

    def convert(self, s, numRows):
        if len(s) <= numRows or numRows == 1:
            return s

        result = []
        for i in range(numRows):
            j = i
            while j < len(s):
                result.append(s[j])
                if (i != 0) and (i != numRows - 1) and (j + (numRows - i - 1) * 2) < len(s):
                    result.append(s[j + (numRows - i - 1) * 2])
                j += (numRows - 1) * 2

        return "".join(result)


testClass = Solution()

a = "PAYPALISHIRING"

print(testClass.convert(a, 3))
