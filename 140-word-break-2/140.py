class Solution(object):

    def wordBreak(self, s, wordDict):
        dp = [0] * (len(s) + 1)

        dp[0]=1
        
        for i in range(1, len(s) + 1):
            for j in range(i):
                print(s[j:i])
                if dp[j] == 1 and s[j:i] in wordDict:
                    dp[i] = 1
                    break
        print(dp)
        sb = []
        for i in range(len(s)):
            sb.append(s[i])
            if dp[i + 1] == 1:
                sb.append(" ")
        print(sb)
        return "".join(sb)


testClass = Solution()


print(testClass.wordBreak("catsanddog", ["cat", "cats", "and", "sand", "dog"]))
