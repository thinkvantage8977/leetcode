class Solution(object):

    def subsetsWithDup(self, nums):
        result = [[]]

        for num in nums:
            for k in result[:]:
                temp = k[:]
                temp.append(num)
                result.append(temp)
        return result


testClass = Solution()

nums = [1, 2, 2]


print(testClass.subsetsWithDup(nums))
