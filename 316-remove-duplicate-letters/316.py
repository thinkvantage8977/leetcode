import collections


class Solution(object):

    def removeDuplicateLetters(self, s):
        d = collections.Counter(s)
        stack = []

        for i in s:
            d[i] -= 1
            if i not in stack:
                while stack and i < stack[-1] and d[stack[-1]] != 0:
                    stack.pop()
                stack.append(i)
        return "".join(stack)


testClass = Solution()
print(testClass.removeDuplicateLetters("bbcaac"))
