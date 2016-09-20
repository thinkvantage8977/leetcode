class myheap(object):

    def __init__(self):
        self.h = [0]

    def perUp(self, i):
        while i // 2 > 0:
            if self.h[i] < self.h[i // 2]:
                self.h[i], self.h[i // 2] = self.h[i // 2], self.h[i]
            i //= 2

    def addValue(self, val):
        self.h.append(val)
        self.perUp(len(self.h) - 1)

    def getMinChildIndex(self, i):
        if i * 2 + 1 > len(self.h) - 1:
            return i * 2
        else:
            return i * 2 if self.h[i * 2] < self.h[i * 2 + 1] else i * 2 + 1

    def perDown(self, i):
        while i * 2 < len(self.h):
            minChild = self.getMinChildIndex(i)
            if self.h[i] > self.h[minChild]:
                self.h[i], self.h[minChild] = self.h[minChild], self.h[i]
            i = minChild

    def popMin(self):
        p = self.h[1]
        self.h[1] = self.h.pop()
        self.perDown(1)
        return p


h = myheap()

h.addValue(1)
h.addValue(2)
h.addValue(3)
h.addValue(4)
h.addValue(-1)
h.addValue(-11)
h.addValue(-111)
h.addValue(1)


print(h.popMin())
print(h.popMin())
print(h.popMin())
print(h.popMin())
print(h.popMin())
