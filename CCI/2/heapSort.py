class Heap(object):

    def __inin__(self):
        self.h = [0]

    def percUp(self, i):
        while i // 2 > 0:
            if self.h[i // 2] > self[i]:
                self.h[i // 2], self.h[i] = self.h[i], self[i // 2]
            i //= 2

    def addMin(self, val):
        self.h.append(val)
        self.percUp(len(self.h) - 1)

    def perDown(self, i):
        while i * 2 < len(self.h):
            midChild = self.minc(i)
            if self.h[midChild] < self.h[i]:
                self.h[midChild], self.h[i] = self.h[i], self.h[midChild]

            i = midChild

    def minc(self, i):
        if i * 2 + 1 > len(self.h) - 1:
            return i * 2
        else:
            return i * 2 if self.h[i * 2] < self.h[i * 2 + 1] else i * 2 + 1

    def deleteMin(self):
        minV = self.h[1]
        self.h[1] = self.h.pop()
        self.perDown(1)
        return minV
