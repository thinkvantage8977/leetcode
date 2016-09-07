class Solution(object):

    def getModifiedArray(self, length, updates):

        l = [0] * (length+1)
        
        for u in updates:
            l[u[0]] += u[2]
            l[u[1] + 1] -= u[2]

        for i in range(1, length):
            l[i] += l[i - 1]
        l.pop()
        return l


testClass = Solution()

length = 5

updates = [
    [1,  3,  2],
    [2,  4,  3],
    [0,  2, -2]
]

print(testClass.getModifiedArray(length, updates))
