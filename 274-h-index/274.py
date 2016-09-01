class Solution(object):

    def merge(self, l1, l2):
        ans = [0] * (len(l1) + len(l2))
        p1 = 0
        p2 = 0
        while p1 < len(l1) and p2 < len(l2):
            if l1[p1] < l2[p2]:
                ans[p1 + p2] = l1[p1]
                p1 += 1
            else:
                ans[p1 + p2] = l2[p2]
                p2 += 1

        while p1 < len(l1):
            ans[p1 + p2] = l1[p1]
            p1 += 1

        while p2 < len(l2):
            ans[p1 + p2] = l2[p2]
            p2 += 1

        return ans

    def mergeSort(self, l):
        if len(l) <= 1:
            return l
        mid = (0 + len(l)) // 2

        left = self.mergeSort(l[:mid])
        right = self.mergeSort(l[mid:])

        return self.merge(left, right)

    def hIndex(self, citations):
        citations = self.mergeSort(citations)
        ans = 0
        for i in range(len(citations)):
            ans = max(ans, min(len(citations) - i, citations[i]))

        return ans


testClass = Solution()

l = [1]

print(testClass.hIndex(l))
