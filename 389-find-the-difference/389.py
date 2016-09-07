class Solution(object):

    def findTheDifference(self, s, t):
        d = collections.Counter(s)

        for i in t:
            if i not in d:
                return i
            else:
                d[i] -= 1
                if d[i] == 0:
                    del d[i]
