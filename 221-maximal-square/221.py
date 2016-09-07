class Solution(object):

    def maximalSquare(self, matrix):
        if not matrix:
        	return 0
        dp = [[0 for i in range(len(matrix[0]))] for j in range(len(matrix))]
        
        result = 0
        
        for i in range(len(matrix[0])):
            if matrix[0][i] == "1":
                dp[0][i] = 1
                result = 1

        for i in range(len(matrix)):
            if matrix[i][0] == "1":
                dp[i][0] = 1
                result = 1

        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[i])):
                if matrix[i][j] == "1":
                    dp[i][j] = min(dp[i - 1][j], dp[i - 1][j - 1], dp[i][j - 1]) + 1
                    result = max(result, dp[i][j])

        return result**2

testClass = Solution()


matrix = ["10100","10111","11111","10010"]

print(testClass.maximalSquare(matrix))
