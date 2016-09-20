class BinaryArraryMinHeap(object):

    def __init__(self):
        self.heapList = []
        self.size = 0

    def percUp(self, i):
        while i // 2 > 0:
            if self.heapList[i] < self.heapList[i // 2]:
                self.heapList[i], self.heapList[i // 2] = self.heapList[i // 2], self.heapList[i]

            i = i // 2

    def insert(self, val):
        self.heapList.append(val)
        self.percUp(len(self.heapList) - 1)

    def getMinChild(self, i):
        if i * 2 + 1 > len(self.heapList) - 1:
            return i * 2
        else:
            return i * 2 + 1 if self.heapList[i * 2 + 1] < self.heapList[i * 2] else i * 2

    def percDown(self, i):

        while i * 2 <= len(self.heapList) - 1:
            minChild = self.getMinChild(i)
            if self.heapList[i] > self.heapList[minChild]:
                self.heapList[i], self.heapList[minChild] = self.heapList[minChild], self.heapList[i]
            i = minChild

    def delMin(self):
        res = self.heapList[1]
        self.heapList[1] = self.heapList.pop()
        self.percDown(1)
        return res
