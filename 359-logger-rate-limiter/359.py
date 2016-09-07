class Logger(object):

    def __init__(self):
        self.recorder = {}

    def shouldPrintMessage(self, timestamp, message):
        if message in self.recorder:
            if timestamp - self.recorder[message] >= 10:
                self.recorder[message] = timestamp
                return True
            else:
                return False
        else:
            self.recorder[message] = timestamp
            return True


testClass = Logger()

print(testClass.shouldPrintMessage(1, "foo"))
print(testClass.shouldPrintMessage(2,"bar"))
print(testClass.shouldPrintMessage(3,"foo"))
print(testClass.shouldPrintMessage(8,"bar"))
print(testClass.shouldPrintMessage(10,"foo"))
print(testClass.shouldPrintMessage(11,"foo"))
