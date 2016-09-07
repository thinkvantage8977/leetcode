import heapq


class Solution(object):

    def kthSmallest(self, matrix, k):
        heapList = []
        markDict = {}
        i = 0
        j = 0
        n = 0
        heapq.heappush(heapList, (matrix[i][j], (i, j)))
        while n < k:

            if j + 1 < len(matrix) and (i, j + 1) not in markDict:
                markDict[(i, j + 1)] = 1
                heapq.heappush(heapList, (matrix[i][j + 1], (i, j + 1)))
            if i + 1 < len(matrix) and (i + 1, j) not in markDict:
                markDict[(i + 1, j)] = 1
                heapq.heappush(heapList, (matrix[i + 1][j], (i + 1, j)))

            res, (i, j) = heapq.heappop(heapList)
            n += 1

        return res


testClass = Solution()

m = [[1,  5,  9],
     [10, 11, 13],
     [12, 13, 15]]


print(testClass.kthSmallest(m, 1))
print(testClass.kthSmallest(m, 2))
print(testClass.kthSmallest(m, 3))
