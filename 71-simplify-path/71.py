class Solution(object):

    def simplifyPath(self, path):
        stack = []
        i = 0
        while i < len(path):
            if path[i] == "/":
                if stack[-1] != "/":
                    stack.append("/")
                i += 1
            elif path[i] == "." and path[i + 1] == ".":
                a = ""
                while a != "//":
                    if stack.empty():
                        stack.append("/")
                        break
                    c = stack.pop()
                    if c == "/":
                        a += c
                i += 2
            elif path[i] == ".":
                i += 1
            else:
                stack.append(path[i])
                i += 1
        res = "".join(stack)
        return res

testClass = Solution()


print(testClass.simplifyPath("/home/"))
