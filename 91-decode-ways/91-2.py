class Solution(object):

    def numDecodings(self, s):
        if not s or s[0] == "0":
            return 0

        if len(s) < 2:
            return 1

        # 排除30 或者00的情况
        for i in range(1, len(s)):
            if s[i] == "0" and (int(s[i - 1]) > 2 or s[i - 1] == "0"):
                return 0

        dp = [0] * len(s)
        dp[0] = 1

        dp[1] = 1 if int(s[:2]) > 26 or s[:2] == "10" or s[:2] == "20" else 2
        print(dp)
        for i in range(2, len(s)):
            # 如果当前是0，那就只能和前一个组合，方案来自DP[I-2]
            if s[i] == "0":
                dp[i] = dp[i - 2]
            # 如果和前一个组合大于26，那就只能SOLO，方案来此DP[I-1]
            elif int(s[i - 1:i + 1]) > 26:
                dp[i] = dp[i - 1]
            # 如果前一个是0，那也只能SOLO
            elif s[i - 1] == "0":
                dp[i] = dp[i - 1]
            # 和前一个可以组合，也可以SOLO，方案来自DP[I-2]+DP[I-1]
            else:
                dp[i] = dp[i - 1] + dp[i - 2]
        print(dp)
        return dp[-1]

testClass = Solution()

print(testClass.numDecodings("227"))
