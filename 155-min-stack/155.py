class MinStack(object):

    def __init__(self):
        self.stack = []
        self.minStack = []
        self.min = 9223372036854775807

    def push(self, x):
        self.stack.append(x)
        if self.min > x:
            self.min = x
        self.minStack.append(self.min)

    def pop(self):
        if len(self.stack) == 0:
            return None
        self.minStack.pop()
        if len(self.minStack) == 0:
            self.min = 9223372036854775807
        else:
            self.min = self.minStack[len(self.minStack) - 1]
        return self.stack.pop()

    def top(self):
        return self.stack[len(self.stack) - 1]

    def getMin(self):
        return self.minStack[len(self.minStack) - 1]


minStack = MinStack()


minStack.push(-2)
minStack.push(0)
minStack.push(-3)
print(minStack.getMin())
print(minStack.pop())
print(minStack.top())
print(minStack.getMin())

