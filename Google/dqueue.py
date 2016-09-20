

import collections

class dqueueForGettingAverage(object):

    def __init__(self, k):
        self.deque = collections.deque()
        self.sum = 0
        self.counter = 0
        self.k = k

        self.precisionCounter = 0

    def add(self, val):

        if self.counter == self.k:
            out = self.deque.pop()
            self.sum -= out
            self.deque.appendleft(val)
            self.sum += val
            self.precisionCounter += 2
        else:
            self.deque.appendleft(val)
            self.counter += 1
            self.sum += val
            self.precisionCounter += 1

    def average(self):

        if self.precisionCounter > 1000:
            self.sum = sum(self.deque)

        return self.sum / float(self.counter)

testClass = dqueueForGettingAverage(5)

testClass.add(1.0)
testClass.add(1.0)
testClass.add(1.0)
testClass.add(1.0)
testClass.add(1.0)
testClass.add(1.0)
testClass.add(1.0)
testClass.add(1.0)
testClass.add(1.0)

print(testClass.average())
testClass.add(2.0)
testClass.add(2.0)
testClass.add(2.0)
print(testClass.average())
