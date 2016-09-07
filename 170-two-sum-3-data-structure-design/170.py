class TwoSum(object):

    def __init__(self):
        self.d = {}
        self.numbers = []

    def add(self, number):
        if number not in self.d:
            self.numbers.append(number)
            self.d[number] = 1
        else:
            self.d[number] += 1

    def find(self, value):

        for n in self.numbers:
            if value - n == n and self.d[n] > 1:
                return True
            elif (value - n) in self.d and value - n != n:
                return True

        return False


# Your TwoSum object will be instantiated and called as such:
# twoSum = TwoSum()
# twoSum.add(number)
# twoSum.find(value)
