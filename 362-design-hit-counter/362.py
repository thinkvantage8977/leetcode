import collections


class HitCounter(object):

    def __init__(self):
        self.queue = collections.deque()

    def hit(self, timestamp):
        self.queue.append(timestamp)

    def getHits(self, timestamp):
        while self.queue and self.queue[0] <= timestamp - 300:
            self.queue.popleft()
        return len(self.queue)
