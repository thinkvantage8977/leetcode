class Solution(object):

    def majorityElement(self, nums):
        major = nums[0]
        count = 1
        for i in range(1, len(nums)):
            if count == 0:
                count = 1
                major = nums[i]
            elif major == nums[i]:
                count += 1
            else:
                count -= 1

        print("major is {},count is {}".format(major, count))
        return major


testClass = Solution()

l = [1, 2, 3, 4, 5, 1, 1, 1, 1, 1, 1, 1, 1, 9]

print(testClass.majorityElement(l))
