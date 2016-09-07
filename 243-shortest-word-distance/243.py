class Solution(object):

    def shortestDistance(self, words, word1, word2):
        i1 = -1
        i2 = -1
        minabs = float("inf")
        for i in range(len(words)):
            if words[i] == word1:
                i1 = i
            elif words[i] == word2:
                i2 = i
            if (i1 != -1 and i2 != -1):
                minabs = min(minabs, abs(i1 - i2))
        return minabs


testClass = Solution()

print(testClass.shortestDistance(["practice", "makes", "perfect", "coding", "makes"], "coding", "practice"))
