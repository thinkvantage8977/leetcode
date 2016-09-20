# 在Data stream中找到median。这道题是Heap的经典应用，需要同时维护一个最大堆和一个最小堆， 
# 最大堆和最小堆的size <= 当前数字count / 2。
# 在学习heap数据结构的时候一般都会讲到这一题，很经典。

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
