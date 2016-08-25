class Solution(object):

    def getRow(self, numRows):
        # result = []
        if numRows == 0:
            return [1]

        current = [1]

        for i in range(0, numRows +1):
            nextLevtl = [1]

            for j in range(0, i - 1):
                nextLevtl.append(current[j] + current[j + 1])
            if i > 0:
                nextLevtl.append(1)

            # result.append(nextLevtl)

            current = nextLevtl

        return current


testClass = Solution()

print(testClass.getRow(0))
print(testClass.getRow(1))
print(testClass.getRow(2))
print(testClass.getRow(3))
print(testClass.getRow(4))
