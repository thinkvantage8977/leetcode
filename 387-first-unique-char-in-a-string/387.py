class Solution(object):

    def firstUniqChar(self, s):
        d = collections.Counter(s)
        for i in range(len(s)):
            if d[s[i]] == 1:
                return i
        return -1
