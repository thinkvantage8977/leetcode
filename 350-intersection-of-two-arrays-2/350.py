class Solution(object):

    def intersect(self, nums1, nums2):
        result = []
        dictN1 = {}
        for n1 in nums1:
            if n1 in dictN1:
                dictN1[n1] += 1
            else:
                dictN1[n1] = 1
        for n2 in nums2:
            if n2 in dictN1:
                dictN1[n2] -= 1
                result.append(n2)
                if dictN1[n2] == 0:
                    del dictN1[n2]
        return result
