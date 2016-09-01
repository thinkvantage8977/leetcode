class Solution(object):

    def pushUp(self, i):
        while i // 2 > 0:
            if self.heapList[i][0] > self.heapList[i // 2][0]:
                self.heapList[i], self.heapList[i // 2] = self.heapList[i // 2], self.heapList[i]
            i //= 2

    def insert(self, val):
        self.heapList.append(val)
        self.pushUp(len(self.heapList) - 1)

    def delMax(self):
        if len(self.heapList) == 2:
            return self.heapList.pop()[1]
        returnValue = self.heapList[1][1]
        self.heapList[1] = self.heapList.pop()
        self.pushDown(1)
        return returnValue

    def pushDown(self, i):
        while (i * 2) <= len(self.heapList) - 1:
            maxChild = self.getMaxChild(i)
            if self.heapList[i][0] < self.heapList[maxChild][0]:
                self.heapList[i], self.heapList[maxChild] = self.heapList[maxChild], self.heapList[i]
            i = maxChild

    def getMaxChild(self, i):
        if i * 2 + 1 > len(self.heapList) - 1:
            return i * 2
        else:
            return i * 2 if self.heapList[i * 2][0] > self.heapList[2 * i + 1][0] else 2 * i + 1

    def topKFrequent(self, nums, k):
        valueDict = {}
        self.heapList = [0]
        for i in nums:
            if i in valueDict:
                valueDict[i] += 1
            else:
                valueDict[i] = 1

        for key, value in valueDict.items():
            self.insert((value, key))

        result = []
        for i in range(k):
            result.append(self.delMax())

        return result


testClass = Solution()

l = [1]

print(testClass.topKFrequent(l, 1))
