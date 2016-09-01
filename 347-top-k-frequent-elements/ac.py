class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        counts = collections.Counter(nums)
        heap = []
        for key, cnt in counts.items():
            if len(heap) < k:
                heapq.heappush(heap, (cnt, key))
            else:
                if heap[0][0] < cnt:
                    heapq.heappop(heap)
                    heapq.heappush(heap, (cnt, key))
        return [x[1] for x in heap]