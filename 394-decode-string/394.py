class Solution(object):

    def decodeString(self, s):

        i = 0
        s1 = ""
        number = ""

        while i < len(s):
            if ord(s[i]) >= 97 and ord(s[i]) <= 122:
                s1 += s[i]
                i += 1
            elif ord(s[i]) >= 48 and ord(s[i]) <= 57:
                number += s[i]
                i += 1
            elif s[i] == "[":
                matchRight = self.nextRightSquareBracket(s, i + 1)
                s1 += int(number) * self.decodeString(s[i + 1:matchRight])
                number = ""
                i = matchRight + 1
        return s1

    def nextRightSquareBracket(self, s, i):
        c = 0
        while i < len(s):
            if s[i] == "[":
                c += 1
                i += 1
            elif s[i] == "]":
                if c == 0:
                    return i
                else:
                    c -= 1
                    i += 1
            else:
                i += 1


testClass = Solution()

print(testClass.decodeString("2[abc]3[cd]ef"))
