import heapq


class Solution(object):

    def rearrangeString(self, str, k):
        if not str:
            return str
        if k ==0:
            return str
        h = []
        d = {}
        for s in str:
            if s not in d:
                d[s] = 1
            else:
                d[s] += 1
        for key, value in d.items():
            heapq.heappush(h, (-value, key))

        ans = []
        l = len(str)
        while l > 0:
            temp = []
            iterationLength = min(l, k)
            if len(h) < iterationLength:
                return ""
            for i in range(iterationLength):
                (value, c) = heapq.heappop(h)
                ans.append(c)
                value += 1
                if value != 0:
                    temp.append((value, c))
                l -= 1
            for i in temp:
                heapq.heappush(h, i)

        return "".join(ans)


testClass = Solution()

print(testClass.rearrangeString("aaadbbcc", 2))
