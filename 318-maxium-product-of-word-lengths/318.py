class Solution(object):

    def maxProduct(self, words):
        bits = [0] * len(words)

        for i in range(0, len(words)):
            for c in words[i]:
                bits[i] |= (1 << (ord(c) - 97))

        maxProduct = 0

        for i in range(0, len(words)):
            for j in range(i + 1, len(words)):
                if (bits[i] & bits[j] == 0) and len(words[i]) * len(words[j]) > maxProduct:
                    maxProduct = len(words[i]) * len(words[j])

        return maxProduct


testClass = Solution()

words = ["a", "aa", "aaa", "aaaa"]

print(testClass.maxProduct(words))
