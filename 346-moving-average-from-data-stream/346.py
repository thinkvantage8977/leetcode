import collections

class MovingAverage(object):

    def __init__(self, size):
        """
        Initialize your data structure here.
        :type size: int
        """
        self.queue = collections.deque(maxlen=size)
        

    def next(self, val):
        """
        :type val: int
        :rtype: float
        """
        queue = self.queue
        queue.append(val)
        return float(sum(queue))/len(queue)

testClass = MovingAverage(3)

print(testClass.next(1))
print(testClass.next(10))
print(testClass.next(3))
print(testClass.next(5))

