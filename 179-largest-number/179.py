class Solution:

    def merge(self, l1, l2):
        result = [""] * (len(l1) + len(l2))
        p1 = 0
        p2 = 0
        while p1 < len(l1) and p2 < len(l2):

            if int(l1[p1] + l2[p2]) > int(l2[p2] + l1[p1]):

                result[p1 + p2] = l1[p1]
                p1 += 1
            else:
                result[p1 + p2] = l2[p2]
                p2 += 1

        while p1 < len(l1):
            result[p1 + p2] = l1[p1]
            p1 += 1

        while p2 < len(l2):
            result[p1 + p2] = l2[p2]
            p2 += 1

        return result

    def mergeSort(self, l):
        if len(l) <= 1:
            return l
        mid = len(l) // 2

        l1 = self.mergeSort(l[:mid])
        l2 = self.mergeSort(l[mid:])

        return self.merge(l1, l2)

    def largestNumber(self, nums):
        strnum = []
        for i in nums:
            strnum.append(str(i))

        result = self.mergeSort(strnum)

        ans = "".join(result)

        for i in range(0, len(ans)):
            if ans[i] != "0":
                return ans[i:]
        return "0"


testClass = Solution()

l = [3, 30, 34, 5, 9]

print(testClass.largestNumber(l))
