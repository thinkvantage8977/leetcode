class Solution(object):
    start = 0
    maxlen = 1

    def longestPalindrome(self, s):
        matrix = [[False for i in range(len(s))] for j in range(len(s))]
        self.preProcess(s, matrix)
        self.DPSearching(s, matrix)
        # print(self.start)
        # print(self.maxlen)

        return s[self.start:self.start + self.maxlen]

    def DPSearching(self, s, matrix):

        # Searching from len 3 to len(s) - i
        for i in range(3, len(s) + 1):
            # Starting position of the string - j
            for j in range(0, len(s) - i + 1):
                # Ending position -K
                k = j + i - 1

                # If the starting position i+1 and ending postion k-1 is true
                # and s[i] == s[k] then matrix[i][k] is true
                if matrix[j + 1][k - 1] and s[j] == s[k]:

                    matrix[j][k] = True

                    if i > Solution.maxlen:
                        #print("j = {}, k ={}, i={}".format(j,k,i))

                        self.start = j
                        self.maxlen = i
        #print (matrix)

    def preProcess(self, s, matrix):
        for x in range(0, len(s)):
            matrix[x][x] = 1
            if x + 1 != len(s) and s[x] == s[x + 1]:
                matrix[x][x + 1] = True
                self.start = x
                self.maxlen = 2

        #print (matrix)


# Setup testClass
testClass = Solution()

s = "esbtzjaaijqkgmtaajpsdfiqtvxsgfvijpxrvxgfumsuprzlyvhclgkhccmcnquukivlpnjlfteljvykbddtrpmxzcrdqinsnlsteonhcegtkoszzonkwjevlasgjlcquzuhdmmkhfniozhuphcfkeobturbuoefhmtgcvhlsezvkpgfebbdbhiuwdcftenihseorykdguoqotqyscwymtjejpdzqepjkadtftzwebxwyuqwyeegwxhroaaymusddwnjkvsvrwwsmolmidoybsotaqufhepinkkxicvzrgbgsarmizugbvtzfxghkhthzpuetufqvigmyhmlsgfaaqmmlblxbqxpluhaawqkdluwfirfngbhdkjjyfsxglsnakskcbsyafqpwmwmoxjwlhjduayqyzmpkmrjhbqyhongfdxmuwaqgjkcpatgbrqdllbzodnrifvhcfvgbixbwywanivsdjnbrgskyifgvksadvgzzzuogzcukskjxbohofdimkmyqypyuexypwnjlrfpbtkqyngvxjcwvngmilgwbpcsseoywetatfjijsbcekaixvqreelnlmdonknmxerjjhvmqiztsgjkijjtcyetuygqgsikxctvpxrqtuhxreidhwcklkkjayvqdzqqapgdqaapefzjfngdvjsiiivnkfimqkkucltgavwlakcfyhnpgmqxgfyjziliyqhugphhjtlllgtlcsibfdktzhcfuallqlonbsgyyvvyarvaxmchtyrtkgekkmhejwvsuumhcfcyncgeqtltfmhtlsfswaqpmwpjwgvksvazhwyrzwhyjjdbphhjcmurdcgtbvpkhbkpirhysrpcrntetacyfvgjivhaxgpqhbjahruuejdmaghoaquhiafjqaionbrjbjksxaezosxqmncejjptcksnoq"

print(testClass.longestPalindrome(s))
