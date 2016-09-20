import bisect


class Solution(object):

    def subArraySumCloestToK(self, array, k):
        sumSet = [0]

        maxSum = -float("inf")
        curSum = 0
        for i in range(len(array)):
            curSum += array[i]

            # trying to find a existing sum such that  thisSum > curSum - k but as samll as possible
            # So k > curSum - thisSum but curSum - thisSum is as large as possible
            # bisect.bisect_left gives you the position for insert value x in sorted array
            # So the index we have will be the ide of the smallest value that larger than curSum-K
            idx = bisect.bisect_left(sumSet, curSum - k)
            if 0 <= idx < len(sumSet):
                maxSum = max(maxSum, curSum - sumSet[idx])

            bisect.insort(sumSet, curSum)

        return maxSum

    def maxSumSubmatrix(self, matrix, k):

        if not matrix:
            return 0

        maxSum = -float("inf")

        # time Complexity O(m*m*nlogn)
        or
        # O(n*n*mlongm)
        if len(matrix[0]) < len(matrix):
            for j in range(len(matrix[0])):
                array = [0] * len(matrix)
                for j1 in range(j, len(matrix[0])):
                    for i in range(len(matrix)):
                        array[i] += matrix[i][j1]
                    maxSum = max(self.subArraySumCloestToK(array, k), maxSum)
        else:
            for i in range(len(matrix)):
                array = [0] * len(matrix[0])
                for i1 in range(i, len(matrix)):
                    for j in range(len(matrix[0])):
                        array[j] += matrix[i1][j]
                    maxSum = max(self.subArraySumCloestToK(array, k), maxSum)

        return maxSum

testClass = Solution()

m = [[1, 0, 1], [0, -2, 3]]


print(testClass.maxSumSubmatrix(m, 2))
