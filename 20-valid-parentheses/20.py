class Solution(object):
    def isValid(self, s):
        stack = []

        valid = ["()","[]","{}"]

        for c in s:
        	if c == '(' or c == '[' or c == '{':
        		stack.append(c)
        	else:
        		if len(stack)==0:
        			return False
        		pair = stack.pop() + c
        		if pair not in valid:
        			return False

        if len(stack)>0:
        	return False

        return True


testClass= Solution()

print(testClass.isValid("[](){}((((()))))("))

