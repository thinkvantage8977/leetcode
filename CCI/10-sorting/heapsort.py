

class BinaryHeap(object):
    """docstring for BinaryHeap"""

    def __init__(self):
        self.heapList = [0]
        self.size = 0

    def printList(self):
        print(self.heapList)

    def percUp(self, i):
        while i // 2 > 0:
            if self.heapList[i] < self.heapList[i // 2]:
                self.heapList[i], self.heapList[i // 2] = self.heapList[i // 2], self.heapList[i]
            i //= 2

    def insert(self, val):
        self.heapList.append(val)
        self.percUp(len(self.heapList) - 1)

    def percDown(self, i):
        while (i * 2) <= len(self.heapList) - 1:
            minChild = self.minChild(i)
            if self.heapList[i] > self.heapList[minChild]:
                self.heapList[i], self.heapList[minChild] = self.heapList[minChild], self.heapList[i]
            i = minChild

    def minChild(self, i):
        if i * 2 + 1 > len(self.heapList) - 1:
            return i * 2
        else:
            return i * 2 if self.heapList[i * 2] < self.heapList[i * 2 + 1] else i * 2 + 1

    def delMin(self):
        returnValue = self.heapList[1]
        self.heapList[1] = self.heapList.pop()
        self.percDown(1)
        return returnValue


testClass = BinaryHeap()


testClass.insert(-1)
testClass.insert(-1)
testClass.insert(-2)
testClass.insert(-3)


testClass.printList()


print("Min = {}".format(testClass.delMin()))

testClass.printList()
