class Solution(object):

    def longestCommonPrefix(self, strs):
        if len(strs) == 0 or not strs or len(strs[0]) == 0:
            return ""

        prefix = []
        i = 0
        c = strs[0][i]
        #print("Hello")
        while i < len(strs[0]):
            c = strs[0][i]
            for s in strs:
                if i >= len(s) or s[i] != c:
                    return "".join(prefix)
            i += 1
            prefix.append(c)

        return "".join(prefix)

testClass = Solution()

strs = [""]


print(testClass.longestCommonPrefix(strs))
