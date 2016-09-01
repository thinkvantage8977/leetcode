class Solution(object):

    def getMinChild(self, i):
        if 2 * i + 1 > len(self.heaplist) - 1:
            return 2 * i
        else:
            return 2 * i if self.heaplist[2 * i] > self.heaplist[2 * i + 1] else 2 * i + 1

    def delMin(self):
        if len(self.heaplist) == 2:
            return self.heaplist.pop()
        returnValue = self.heaplist[1]
        self.heaplist[1] = self.heaplist.pop()
        self.prcuDown(1)
        return returnValue

    def prcuDown(self, i):
        while i * 2 <= len(self.heaplist) - 1:
            minChild = self.getMinChild(i)

            if self.heaplist[i] < self.heaplist[minChild]:
                self.heaplist[i], self.heaplist[
                    minChild] = self.heaplist[minChild], self.heaplist[i]

            i = minChild

    def prcuUP(self, i):
        while i // 2 > 0:
            if self.heaplist[i] > self.heaplist[i // 2]:
                self.heaplist[i], self.heaplist[
                    i // 2] = self.heaplist[i // 2], self.heaplist[i]
            i //= 2

    def insert(self, val):
        self.heaplist.append(val)
        self.prcuUP(len(self.heaplist) - 1)

    def findKthLargest(self, nums, k):
        self.heaplist = [0]

        for i in nums:
            self.insert(i)

        for i in range(k):
            returnValue = self.delMin()

        return returnValue


testClass = Solution()


l = [3, 2, 1, 5, 6, 4]

# l = [2, 1]


print(testClass.findKthLargest(l, 2))
