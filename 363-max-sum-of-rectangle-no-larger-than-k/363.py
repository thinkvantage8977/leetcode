
import bisect


class Solution(object):

    def maxSubArray(self, array):
        maxSum = 0
        localStart = 0
        maxStart = 0
        maxEnd = -1
        s = 0
        for i in range(len(array)):
            s += array[i]
            if s < 0:
                s = 0
                localStart = i + 1
            elif s > maxSum:
                maxSum = s
                maxStart = localStart
                maxEnd = i
        if maxEnd != -1:
            return (maxSum, maxStart, maxEnd)
        else:
            maxSum = -float("inf")
            for i in range(len(array)):
                if array[i] > maxSum:
                    maxSum = array[i]
                    maxStart = i
                    maxEnd = i

        return (maxSum, maxStart, maxEnd)

    def maxSubArraySum(self, array):
        maxSum = array[0]
        localSum = array[0]
        for i in range(1, len(array)):
            localSum = max(array[i], localSum + array[i])
            maxSum = max(maxSum, localSum)
        return maxSum

    def maxSubArraylessK(self, nums, k):
        """
        we need to find the sum[right]-sum[left]<=k
        since the bitsect return the index of the sorted value
        we can't directly pop the nums[idx] 
        we should use insort from the bisect
        """
        # python set() doesn't support indexing, using list instead
        # similar as the c++ or java set()

        cumset = []
        cumset.append(0)
        maxsum = -float("inf")
        cursum = 0
        for i in range(len(nums)):
            cursum += nums[i]
            # find the lower bound of the index
            idx = bisect.bisect_left(cumset, cursum - k)
            # find max in sum[right]-sum[left]<=k
            if 0 <= idx < len(cumset):
                maxsum = max(maxsum, cursum - cumset[idx])
            # using insort instead of append since bisect_left reason
            bisect.insort(cumset, cursum)
        return maxsum

    def maxSumSubmatrix(self, matrix, k):
        if not matrix:
            return 0

        maxSubMatrix = -float("inf")
        for j in range(len(matrix[0])):
            colSum = [0] * len(matrix)
            for l in range(j, len(matrix[0])):
                for i in range(len(matrix)):
                    colSum[i] += matrix[i][l]
                maxSubMatrix = max(maxSubMatrix, self.maxSubArraylessK(colSum, k))
        return maxSubMatrix


testClass = Solution()

m = [[1,  0, 1], [0, -2, 3]]


print(testClass.maxSumSubmatrix([[2, 2, -1]], 3))

# print(testClass.maxSubArraylessK([3], 3))
