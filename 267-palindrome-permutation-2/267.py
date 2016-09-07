import collections


class Solution(object):

    def DFS(self, current, l, s):
        if current == l:
            firsthalf = "".join(s)
            secondhalf = "".join(s[::-1])
            if (firsthalf + self.middle + secondhalf) not in self.res:
                self.res[firsthalf + self.middle + secondhalf] = 1
        else:
            for i in range(l):
                if self.table[i] == False:
                    self.table[i] = True
                    s.append(self.candidate[i])
                    self.DFS(current + 1, l, s)
                    s.pop()
                    self.table[i] = False

    def generatePalindromes(self, s):
        cdict = collections.Counter(s)
        self.middle = ""
        self.candidate = []
        for key, value in cdict.items():
            if value % 2 == 1:
                if self.middle != "":
                    return []
                else:
                    self.middle = key
            for j in range(value // 2):
                self.candidate.append(key)

        l = len(self.candidate)

        self.table = [False] * l
        self.res = {}
        self.DFS(0, l, [])

        return list(self.res.keys())


testClass = Solution()

print(testClass.generatePalindromes("aaaaaa"))
