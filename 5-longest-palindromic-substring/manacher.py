class Solution(object):

    def preProcess(self, s):
        news = []
        for c in s:
            news.append("#")
            news.append(c)
        news.append("#")
        return "".join(news)

    def longestPalindrome(self, s):
        olds = s
        s = self.preProcess(s)
        p = [0] * len(s)

        c = 0
        r = 0

        for i in range(1, len(s) - 1):
            mirrorI = 2 * c - i
            p[i] = min(r - i, p[mirrorI]) if r > i else 0

            while i + p[i] + 1 < len(s) and s[i + p[i] + 1] == s[i - p[i] - 1]:
                p[i] += 1

            if (i + p[i]) > r:
                c = i
                r = i + p[i]

        maxL = 0
        position = 0
        for i in range(len(p)):
            if p[i] > maxL:
                maxL = p[i]
                position = i
        print("p ={}, max={}".format(position, maxL))
        return olds[(position - maxL ) // 2:(position - maxL ) // 2 + maxL]


testClass = Solution()

s = "esbtzjaaijqkgmtaajpsdfiqtvxsgfvijpxrvxgfumsuprzlyvhclgkhccmcnquukivlpnjlfteljvykbddtrpmxzcrdqinsnlsteonhcegtkoszzonkwjevlasgjlcquzuhdmmkhfniozhuphcfkeobturbuoefhmtgcvhlsezvkpgfebbdbhiuwdcftenihseorykdguoqotqyscwymtjejpdzqepjkadtftzwebxwyuqwyeegwxhroaaymusddwnjkvsvrwwsmolmidoybsotaqufhepinkkxicvzrgbgsarmizugbvtzfxghkhthzpuetufqvigmyhmlsgfaaqmmlblxbqxpluhaawqkdluwfirfngbhdkjjyfsxglsnakskcbsyafqpwmwmoxjwlhjduayqyzmpkmrjhbqyhongfdxmuwaqgjkcpatgbrqdllbzodnrifvhcfvgbixbwywanivsdjnbrgskyifgvksadvgzzzuogzcukskjxbohofdimkmyqypyuexypwnjlrfpbtkqyngvxjcwvngmilgwbpcsseoywetatfjijsbcekaixvqreelnlmdonknmxerjjhvmqiztsgjkijjtcyetuygqgsikxctvpxrqtuhxreidhwcklkkjayvqdzqqapgdqaapefzjfngdvjsiiivnkfimqkkucltgavwlakcfyhnpgmqxgfyjziliyqhugphhjtlllgtlcsibfdktzhcfuallqlonbsgyyvvyarvaxmchtyrtkgekkmhejwvsuumhcfcyncgeqtltfmhtlsfswaqpmwpjwgvksvazhwyrzwhyjjdbphhjcmurdcgtbvpkhbkpirhysrpcrntetacyfvgjivhaxgpqhbjahruuejdmaghoaquhiafjqaionbrjbjksxaezosxqmncejjptcksnoq"
# s = "abba"
print(testClass.longestPalindrome(s))
