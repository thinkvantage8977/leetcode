class Solution(object):

    def simplifyPath(self, path):
        l = path.split("/")
        stack = []
        for i in range(len(l)):
            if l[i] == "..":
                if stack:
                    stack.pop()
                continue
            if l[i] == "":
                continue
            if l[i] == ".":
                continue
            stack.append(l[i])

        return "/" + "/".join(stack)

testClass = Solution()


print(testClass.simplifyPath("/.."))
