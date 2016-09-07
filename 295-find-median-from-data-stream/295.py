import heapq


class MedianFinder:

    def __init__(self):
        self.minHeap = []
        self.maxHeap = []

    def addNum(self, num):
        heapq.heappush(self.maxHeap, num * -1)
        heapq.heappush(self.minHeap, heapq.heappop(self.maxHeap) * -1)

        if len(self.maxHeap) < len(self.minHeap):
            heapq.heappush(self.maxHeap, heapq.heappop(self.minHeap) * -1)

    def findMedian(self):

        if len(self.maxHeap) == len(self.minHeap):
            return float(((self.maxHeap[0] * -1) + self.minHeap[0])) / 2
        else:
            return float(self.maxHeap[0] * -1)


# Your MedianFinder object will be instantiated and called as such:
mf = MedianFinder()
mf.addNum(2)

print(mf.findMedian())

mf.addNum(3)

print(mf.findMedian())
