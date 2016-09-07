


class Solution(object):

    def preProcess(self, s):
        news = []
        for c in s:
            news.append("#")
            news.append(c)
        news.append("#")
        return "".join(news)

    def shortestPalindrome(self, s):
        olds = s
        s = self.preProcess(s)
        c = 0
        r = 0
        p = [0] * len(s)
        for i in range(1, len(s) - 1):
            mirrorI = 2 * c - i
            p[i] = min(r - i, p[mirrorI]) if r > i else 0

            while i + p[i] + 1 < len(s) and s[i + p[i] + 1] == s[i - p[i] - 1]:
                p[i] += 1

            if (i + p[i]) > r:
                c = i
                r = i + p[i]

        center = 0  
        for i in range(1, len(s) - 1):
            if p[i] == i:
                center=p[i]
        print(center)
        return olds[center:][::-1] + olds


testClass=Solution()
s="ab"
print(testClass.shortestPalindrome(s))
