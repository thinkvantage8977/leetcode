import heapq


class Solution(object):

    def rearrangeString(self, str, k):
        if k == 0:
            return str
        charDict = {}

        heap = [(-f, c) for c, f in collections.Counter(str).items()]

        heapq.heapify(heap)

        l = len(str)
        ans = []

        while l > 0:
            length = min(k, l)
            temp = []
            if len(heap) < length:
                return ""
            for i in range(0, length):
                current = heapq.heappop(heap)
                ans.append(current[1])
                l -= 1
                if current[0] + 1 != 0:
                    temp.append((current[0] + 1, current[1]))

            for i in temp:
                heapq.heappush(heap, i)

        return "".join(ans)


testClass = Solution()

print(testClass.rearrangeString("aabbcc", 3))
