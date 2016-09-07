import collections


class Solution(object):

    def getHint(self, secret, guess):
        bull = 0
        cow = 0

        s = collections.Counter(secret)
        g = collections.Counter(guess)
        
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                bull += 1
                s[secret[i]] -= 1
                if s[secret[i]] == 0:
                    del s[secret[i]]
                g[secret[i]] -= 1
                if g[secret[i]] == 0:
                    del g[secret[i]]

        for key, value in g.items():

            for j in range(value):
                if key in s:
                    cow += 1
                    s[key] -= 1
                    if s[key] == 0:
                        del s[key]

        return str(bull) + "A" + str(cow) + "B"


testClass = Solution()

print(testClass.getHint("1123","0111"))