class Solution(object):

    def decodeString(self, s):
        if not s:
            return s

        i = 0
        res = []
        counter = ""
        while i < len(s):
            if s[i] in "0123456789":
                counter += s[i]
                i += 1
            elif 96 < ord(s[i]) < 123:
                res.append(s[i])
                i += 1
            elif s[i] == "[":
                matachRight = self.findMatchingRight(i + 1, s)
                res.append(int(counter) * self.decodeString(s[i + 1:matachRight]))
                counter = ""
                i = matachRight + 1

        return "".join(res)

    def findMatchingRight(self, i, s):
        left = 0
        while i < len(s):
            if s[i] == "[":
                left += 1

            elif s[i] == "]":
                if left == 0:
                    return i
                else:
                    left -= 1
            i += 1


testClass = Solution()

print(testClass.decodeString("3[a]2[bc]"))
