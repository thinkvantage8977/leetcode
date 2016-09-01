class Solution(object):

    def intToRoman(self, num):
        mathDict = {1: "I", 5: "V", 10: "X",
                    50: "L", 100: "C", 500: "D", 1000: "M"}
        n = num
        result = ""
        count = 0

        while n != 0:
            d = n % 10
            s = ""
            if d in [1, 2, 3]:
                s = mathDict[1 * (10**count)] * (d)
            elif d in [4]:
                s = mathDict[1 * (10**count)] + mathDict[5 * (10**count)]
            elif d in [5, 6, 7, 8]:
                s = mathDict[5 * (10**count)] + \
                    mathDict[1 * (10**count)] * (d - 5)
            elif d in [9]:
                s = mathDict[(10**count)] + mathDict[(10**(count + 1))]
            count += 1
            n = n // 10
            result = s + result
        return result


testClass = Solution()

print(testClass.intToRoman(10))
print(testClass.intToRoman(11))
print(testClass.intToRoman(1123))
print(testClass.intToRoman(3999))
