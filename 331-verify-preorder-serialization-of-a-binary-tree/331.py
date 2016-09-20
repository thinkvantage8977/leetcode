class Solution(object):

    def isValidSerialization(self, preorder):
        l = preorder.split(",")[::-1]
        stack = []
        if not l :
            return False
        while len(l) > 0:
            stack.append(l.pop())
            while len(stack) > 2 and stack[-1] == stack[-2] == "#":
                stack.pop()
                stack.pop()
                num = stack.pop()
                if num == "#":
                    return False
                stack.append("#")

        if len(stack)==1 and stack[0] == "#":
            return True
        else:
            return False


testClass = Solution()

print(testClass.isValidSerialization("9,#,#,1"))
