class Solution(object):

    def strStr(self, haystack, needle):
        if not haystack and not needle:
            return 0

        if len(needle) > len(haystack):
            return -1
        for i in range(0, len(haystack)):
            # print(haystack[i:i + len(needle)])
            if haystack[i:i + len(needle)] == needle:
                return i
        return -1


testClass = Solution()

print(testClass.strStr("1231234123", "1234"))
