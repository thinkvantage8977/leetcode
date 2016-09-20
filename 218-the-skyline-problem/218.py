class maxHeapWithDelete(object):

    def __init__(self):
        self.h = [0]

    def percUp(self, i):
        while i // 2 > 0:
            if self.h[i] > self.h[i // 2]:
                self.h[i], self.h[i // 2] = self.h[i // 2], self.h[i]
            i //= 2

    def add(self, val):
        self.h.append(val)
        self.percUp(len(self.h) - 1)

    def popMax(self):
        res = self.h[1]
        self.h[1] = self.h.pop()
        self.percDown(1)
        return res

    def percDown(self, i):
        while i * 2 <= len(self.h) - 1:
            maxChild = self.getMaxChild(i)
            if self.h[maxChild] > self.h[i]:
                self.h[maxChild], self.h[i] = self.h[i], self.h[maxChild]
            i = maxChild

    def getMaxChild(self, i):
        if i * 2 + 1 > len(self.h) - 1:
            return i * 2
        return i * 2 if self.h[i * 2] > self.h[i * 2 + 1] else i * 2 + 1

    def top(self):
        return self.h[1]

    def delete(self, val):
        for i in range(1, len(self.h)):
            if self.h[i] == val:
                break
        if i == len(self.h) - 1:
            self.h.pop()
        else:
            self.h[i] = self.h.pop()
            self.percDown(i)


class Solution(object):

    def getSkyline(self, buildings):
        if not buildings:
            return []

        l = []

        for i in buildings:
            l.append((i[0], i[2], 0))
            l.append((i[1], i[2], 1))

        l.sort(key=lambda x: (x[0], x[1]))

        print(l)
        maxHeap = maxHeapWithDelete()

        res = []

        preiousMaxHeight = 0

        maxHeap.add(0)

        for p in l:
            if p[2] == 0:
                maxHeap.add(p[1])
            else:
                maxHeap.delete(p[1])
            if maxHeap.top() != preiousMaxHeight:
                res.append([p[0], maxHeap.top()])
                preiousMaxHeight = maxHeap.top()

        return res

l = [[2, 9, 10], [3, 7, 15], [5, 12, 12], [15, 20, 10], [19, 24, 8]]

l = [[0, 2, 3], [2, 5, 3]]

l= [[1,2,1],[1,2,2],[1,2,3]]

testClass = Solution()

print(testClass.getSkyline(l))
