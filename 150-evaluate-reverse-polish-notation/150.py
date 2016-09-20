class Solution(object):

    def evalRPN(self, tokens):
        stack = []

        i = 0

        while i < len(tokens):
            if tokens[i] not in ["+", "-", "*", "/"]:
                stack.append(int(tokens[i]))
            else:
                a1 = stack.pop()
                a2 = stack.pop()

                if tokens[i] == "+":
                    stack.append(a1 + a2)
                if tokens[i] == "-":
                    stack.append(a2 - a1)
                if tokens[i] == "*":
                    stack.append(a1 * a2)
                if tokens[i] == "/":
                    stack.append(int(float(a2)/a1))
            i += 1

        return stack[0]


testClass = Solution()

print(testClass.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))
