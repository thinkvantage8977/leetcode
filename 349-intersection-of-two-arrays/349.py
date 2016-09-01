class Solution(object):

    def intersection(self, nums1, nums2):
        result = []
        for n1 in set(nums1):
            if n1 in nums2:
                result.append(n1)
        return result
