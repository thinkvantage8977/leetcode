class Solution(object):

    def twoSum(self, nums, i, j, q):
        while i < j:
            if nums[i] + nums[j] + q == 0:
                self.res.append([q, nums[i], nums[j]])
                while i < j and nums[i] == nums[i + 1]:
                    i += 1
                while i < j and nums[j] == nums[j - 1]:
                    j -= 1
                i += 1
                j -= 1
            else:
                if nums[i] + nums[j] + q < 0:
                    i += 1
                else:
                    j -= 1

    def threeSum(self, nums):

        if len(nums) < 3:
            return []

        nums.sort()
        i = 0

        self.res = []

        while i < len(nums) - 2:
            if i!=0 and nums[i] == nums[i - 1]:
                i += 1
                continue
            q = nums[i]
            self.twoSum(nums, i + 1, len(nums) - 1, q)
            i += 1

        return self.res

testClass = Solution()

print(testClass.threeSum([0, 0, 0]))
