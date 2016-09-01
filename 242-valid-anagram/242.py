class Solution(object):

    def isAnagram(self, s, t):
        d = {}
        for c in s:
            if c not in d:
                d[c] = 1
            else:
                d[c] += 1
        for c in t:
            if c not in d:

                return False
            else:
                d[c] -= 1
                if d[c] == 0:
                    del d[c]
        if not d:
            return True
        else:
            return False


testClass = Solution()

print(testClass.isAnagram("anagram", "nagaram"))
