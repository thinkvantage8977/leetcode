class Solution(object):

    def merge(self, nums1, m, nums2, n):
        total = m + n

        while m != 0 and n != 0:
            print("m= {}, n={}".format(m, n))

            if nums1[m - 1] > nums2[n - 1]:
                nums1[total - 1] = nums1[m - 1]
                total -= 1
                m -= 1
            else:
                nums1[total - 1] = nums2[n - 1]
                total -= 1
                n -= 1

        while m != 0:
            nums1[total - 1] = nums1[m - 1]
            total -= 1
            m -= 1

        while n != 0:
            nums1[total - 1] = nums2[n - 1]
            total -= 1
            n -= 1


l1 = [0]
l2 = [1]

testClass = Solution()
testClass.merge(l1, 0, l2, 1)
print(l1)
