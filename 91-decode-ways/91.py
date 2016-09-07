class Solution(object):

    def numDecodings(self, s):
        if not s:
            return 0

        if s[0] == "0":
            return 0

        if len(s) == 1:
            return 1

        dp = [0] * len(s)
        dp[0] = 1

        if int(s[0] + s[1]) <= 26 and s[1] != "0":
            dp[1] = 2
        elif int(s[0] + s[1]) > 26 and s[1] == "0":
        	return 0
        else:
            dp[1] = 1

        for i in range(2, len(s)):
            if s[i] == "0" and s[i - 1] == "0":
                return 0
            elif s[i] == "0" and int(s[i - 1] + s[i]) > 26:
                return 0
            elif s[i] == "0" and int(s[i - 1] + s[i]) <= 26:
                dp[i] = dp[i - 2]

            elif s[i - 1] == "0":
                dp[i] = dp[i - 1]
            elif int(s[i - 1] + s[i]) <= 26:
                dp[i] = dp[i - 1] + dp[i - 2]
            else:
                dp[i] = dp[i - 1]
        print(dp)
        return dp[-1]


testClass = Solution()


print(testClass.numDecodings("101"))
