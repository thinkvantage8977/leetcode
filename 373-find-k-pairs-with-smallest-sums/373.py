import heapq


class Solution(object):

    def kSmallestPairs(self, nums1, nums2, k):

        if not nums1 or not nums2:
            return []

        heap = []
        for i in range(min(k, len(nums1))):
            for j in range(min(k, len(nums2))):
                heapq.heappush(heap, (nums1[i] + nums2[j], nums1[i], nums2[j]))
        ans = []

        while k > 0 and heap:
            a = heapq.heappop(heap)
            ans.append([a[1], a[2]])
            k -= 1
        return ans


testClass = Solution()

nums1 = [-10, 0, 10]
nums2 = [1, 2, 3]

print(testClass.kSmallestPairs(nums1, nums2, 10))
