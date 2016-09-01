class Solution(object):

    def wiggleSort(self, nums):
        temp = sorted(nums)
        mid, l = (len(nums) + 1) >> 1, len(nums)
        for i in range(len(nums)):
            if i & 1 == 0:
                mid -= 1
                nums[i] = temp[mid]
            else:
                l -= 1
                nums[i] = temp[l]
