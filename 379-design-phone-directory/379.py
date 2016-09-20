class PhoneDirectory(object):

    def __init__(self, maxNumbers):
        self.s = set()
        for i in range(maxNumbers):
            self.s.add(i)

    def get(self):
        if len(self.s) == 0:
            return -1
        else:
            return self.s.pop()

    def check(self, number):
        if number in self.s:
            return True
        else:
            return False

    def release(self, number):
        self.s.add(number)


# Your PhoneDirectory object will be instantiated and called as such:
# obj = PhoneDirectory(maxNumbers)
# param_1 = obj.get()
# param_2 = obj.check(number)
# obj.release(number)
