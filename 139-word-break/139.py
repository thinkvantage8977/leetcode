class Solution(object):

    def wordBreak(self, s, wordDict):
        if not wordDict:
            return not s

        dp = [0] * (len(s) + 1)

        dp[0] = 1

        for i in range(1, len(s) + 1):
            for j in range(0, i):
                if dp[j] == 1 and s[j:i] in wordDict:
                    dp[i] = 1
                    break

        return True if dp[-1]==1 else False


testClass = Solution()

print(testClass.wordBreak("leetcode", ["leet", "code"]))
