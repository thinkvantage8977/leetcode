class Solution(object):

    def reduce(self, s):
        number = []
        for c in s:
            number.append(c)
        while number[0] != "a":
            for i in range(len(number)):
                number[i] = chr(ord(number[i]) - 1)
                if ord(number[i]) == 96:
                    number[i] = "z"

        return "".join(number)

    def groupStrings(self, strings):
        d = {}

        for i in strings:
            r = self.reduce(i)

            if r in d:
                d[r].append(i)
            else:
                d[r] = [i]
        res = []
        for key, value in d.items():
            res.append(value)

        return res


testClass = Solution()

ss = ["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"]

print(testClass.groupStrings(ss))
