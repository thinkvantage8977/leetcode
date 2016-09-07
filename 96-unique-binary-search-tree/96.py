class Solution(object):

    def numTrees(self, n):
        f = [0] * (n+1)
        f[0] = 1

        for i in range(1, n+1):
        	for j in range(0,i):
        		f[i] += f[j]*f[i-1-j]

        	


        return f[n]


testClass = Solution()

print(testClass.numTrees(3))
