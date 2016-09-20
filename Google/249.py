class Solution(object):

    def hash(self, s):
        d = []
        for c in s:
            d.append(ord(c) - 97)
        distance = 25 - d[0]
        for i in range(len(d)):
            d[i] += distance
            d[i] -= 26 if d[i] > 25 else 0

        res = []
        for i in d:
            res.append(chr(i + 97))
        return "".join(res)

    def groupStrings(self, strs):
        if not strs:
            return []

        d = {}

        for s in strs:
            hashcode = self.hash(s)
            if hashcode not in d:
                d[hashcode] = [s]
            else:
                d[hashcode].append(s)

        res = []
        # print(d)
        for key, value in d.items():
            res.append(value)

        return res


testClass = Solution()
print(testClass.groupStrings(["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"]))
