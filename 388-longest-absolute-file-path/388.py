class Solution(object):

    def countLevel(self, s):
        c = 0
        for i in s:
            if i == '\t':
                c += 1
        return c

    def lengthLongestPath(self, input):
        if not input:
            return 0

        stack = []
        maxLength = 0
        l = input.split("\n")

        for i in range(len(l)):
            #count number of "\t" in a string represting the correct level for this dir/file
            levelCount = self.countLevel(l[i])

            #pop the stack untile it matches the correct level
            while levelCount < len(stack):
                stack.pop()

            currentTop = stack[-1] if stack else -1
            
            if "." in l[i]:
                maxLength = max(maxLength, 1 + len(l[i]) - levelCount + currentTop)
            else:
                stack.append(1 + len(l[i]) - levelCount + currentTop)
                print(stack)

        return maxLength


testClass = Solution()

print(testClass.lengthLongestPath("dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"))
print(testClass.lengthLongestPath("a.txt"))
