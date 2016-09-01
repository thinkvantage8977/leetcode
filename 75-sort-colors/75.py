class Solution(object):

    def sortColors(self, nums):
        i = 0
        j = len(nums) - 1
        k = len(nums) - 1

        while i <= j:
            if nums[i] == 2:
                nums[i], nums[k] = nums[k], nums[i]
                k -= 1
                if k < j:
                    j = k
            elif nums[i] == 1:
                nums[i], nums[j] = nums[j], nums[i]
                j -= 1
            else:
                i += 1
