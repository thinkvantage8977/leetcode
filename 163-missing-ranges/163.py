class Solution(object):

    def findMissingRanges(self, nums, lower, upper):
        nums = [lower - 1] + nums + [upper + 1]
        p1 = 0
        p2 = 1
        res = []
        if len(nums) < 2:
            return []

        while p2 < len(nums):
            if nums[p2] - nums[p1] <= 1:
                p1 += 1
                p2 += 1
                continue
            if nums[p2] - nums[p1] == 2:
                res.append(str(nums[p1] + 1))
                p1 += 1
                p2 += 1
                continue
            else:
                res.append(str(nums[p1] + 1) + "->" + str(nums[p2] - 1))
                p1 += 1
                p2 += 1

        return res


testClass = Solution()

print(testClass.findMissingRanges([0, 1, 3, 50, 75], 0, 99))
