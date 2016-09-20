
# 在优先队列中存储以(数量+字符)的对, 以k为区间大小排列k个从数量高到低的字符, 
# 然后再重复此过程, 这种贪心的策略可以保证让数量大的最优先排列, 
# 并且使其间隔最小的距离, 否则到后来可能没有足够的空间.
import heapq

class Solution(object):

    def rearrangeString(self, str, k):
        if k == 0:
            return str
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
