class Solution(object):

    def longestPalindrome(self, s):
        if not s:
            return None
        
        l = len(s)
        dp = [[False for i in range(l)] for j in range(l)]

        longest = 1
        start = 0

        for i in range(l):
            dp[i][i] = True
            if i + 1 < l and s[i] == s[i + 1]:
                dp[i][i + 1] = True
                longest = 2
                start = i

        # i = length of the string
        for i in range(2, l + 1):

            for j in range(0, l - i + 1):

                endPosition = i + j - 1

                if dp[j + 1][endPosition - 1] == True and s[j] == s[endPosition]:
                    dp[j][endPosition] = True

                    if i > longest:
                        longest = i
                        start = j


        return s[start:start + longest]


# Setup testClass
testClass = Solution()


s = "esbtzjaaijqkgmtaajpsdfiqtvxsgfvijpxrvxgfumsuprzlyvhclgkhccmcnquukivlpnjlfteljvykbddtrpmxzcrdqinsnlsteonhcegtkoszzonkwjevlasgjlcquzuhdmmkhfniozhuphcfkeobturbuoefhmtgcvhlsezvkpgfebbdbhiuwdcftenihseorykdguoqotqyscwymtjejpdzqepjkadtftzwebxwyuqwyeegwxhroaaymusddwnjkvsvrwwsmolmidoybsotaqufhepinkkxicvzrgbgsarmizugbvtzfxghkhthzpuetufqvigmyhmlsgfaaqmmlblxbqxpluhaawqkdluwfirfngbhdkjjyfsxglsnakskcbsyafqpwmwmoxjwlhjduayqyzmpkmrjhbqyhongfdxmuwaqgjkcpatgbrqdllbzodnrifvhcfvgbixbwywanivsdjnbrgskyifgvksadvgzzzuogzcukskjxbohofdimkmyqypyuexypwnjlrfpbtkqyngvxjcwvngmilgwbpcsseoywetatfjijsbcekaixvqreelnlmdonknmxerjjhvmqiztsgjkijjtcyetuygqgsikxctvpxrqtuhxreidhwcklkkjayvqdzqqapgdqaapefzjfngdvjsiiivnkfimqkkucltgavwlakcfyhnpgmqxgfyjziliyqhugphhjtlllgtlcsibfdktzhcfuallqlonbsgyyvvyarvaxmchtyrtkgekkmhejwvsuumhcfcyncgeqtltfmhtlsfswaqpmwpjwgvksvazhwyrzwhyjjdbphhjcmurdcgtbvpkhbkpirhysrpcrntetacyfvgjivhaxgpqhbjahruuejdmaghoaquhiafjqaionbrjbjksxaezosxqmncejjptcksnoq"

# s = "aa"

print(testClass.longestPalindrome(s))
