class Solution(object):

    def generate(self, numRows):
        result = []
        if numRows == 0:
            return result

        current = [1]

        for i in range(0, numRows):
            nextLevtl = [1]

            
            for j in range(0, i - 1):
                nextLevtl.append(current[j] + current[j + 1])
            if i > 0:
                nextLevtl.append(1)

            result.append(nextLevtl)
            
            current = nextLevtl

        return result


testClass = Solution()

print(testClass.generate(1))
