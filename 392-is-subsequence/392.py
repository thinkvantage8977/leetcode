class Solution(object):

    def isSubsequence(self, s, t):
    	if not s:
    		return True
    	if not t:
    		return False
        s = s[::-1]
        stack = []
        for c in s:
            stack.append(c)

        for c in t:
            if c == stack[-1]:
                stack.pop()
                if stack == []:
                	return True

        return False
