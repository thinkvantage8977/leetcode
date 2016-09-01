class Solution(object):

    def romanToInt(self, s):
        mathDict = {"I": 1, "V": 5, "X": 10,
                    "L": 50, "C": 100, "D": 500, "M": 1000}
        result = 0
        previous = "I"

        for c in s[::-1]:
            result = result - \
                mathDict[c] if mathDict[c] < mathDict[
                    previous] else result + mathDict[c]
            previous = c
        return result


testClass = Solution()

print(testClass.romanToInt("MMMDCCCLXXXVIII"))
