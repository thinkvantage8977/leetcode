class Solution(object):

    def addBinary(self, a, b):
        a = a[::-1]
        b = b[::-1]
        pa = 0
        pb = 0
        res = []
        while pa < len(a) or pb < len(b):
            avalue = int(a[pa]) if pa < len(a) else 0
            pa = pa + 1 if pa < len(a) else pa
            bvalue = int(b[pb]) if pb < len(b) else 0
            pb = pb + 1 if pb < len(b) else pb
            res.append(avalue + bvalue)
        c = 0
        print(res)
        for i in range(len(res)):
            res[i] += c
            if res[i] == 2:
                c = 1
                res[i] = 0
            elif res[i] == 3:
                c =1
                res[i] =1
            else:
                c = 0

        if c == 1:
            res.append(1)

        s = []
        for d in res:
            s.append(str(d))

        return "".join(s)[::-1]


testClass = Solution()

print(testClass.addBinary("111", "111"))
