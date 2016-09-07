class Solution(object):

    def checkPalindrome(self, l):
        for i in range(len(l) // 2):
            if l[i] != l[len(l) - i - 1]:
                return False
        return True

    def palindromePairs(self, words):
        rwordDict = {}
        special = -1
        for i in range(len(words)):
            rwordDict[words[i][::-1]] = i
            if words[i] == "":
                special = i
        res = []

        if special != -1:
            for i in range(len(words)):
                if i != special and self.checkPalindrome(words[i]):
                    res.append([i, special])
                    res.append([special, i])

        for i in range(len(words)):
            word = words[i]

            for j in range(1, len(word) + 1):
                if word[:j] in rwordDict and self.checkPalindrome(word[j:]) and i != rwordDict[word[:j]]:
                    res.append([i, rwordDict[word[:j]]])

            for j in range(1, len(word)):
                if word[j:] in rwordDict and self.checkPalindrome(word[:j]) and i != rwordDict[word[j:]]:
                    res.append([rwordDict[word[j:]], i])

        return res

testClass = Solution()

l = ["a", ""]

print(testClass.palindromePairs(l))
