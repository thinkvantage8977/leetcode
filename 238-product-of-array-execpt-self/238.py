class Solution(object):

    def productExceptSelf(self, nums):
        l = [1] * len(nums)
        r = [1] * len(nums)

        for i in range(1, len(nums)):
            l[i] = l[i - 1] * nums[i - 1]

        for j in range(len(nums) - 2, 0, -1):
            r[j] = r[j + 1] * nums[j + 1]

        res = [0] * len(nums)

        res[0] = r[1] * nums[1]
        res[-1] = l[-2] * nums[-2]
        print(l)
        print(r)
        for i in range(1, len(nums) - 1):
            res[i] = l[i] * r[i]
        return res

testClass = Solution()

l = [1, 2, 3, 4,5,6,7]

print(testClass.productExceptSelf(l))
