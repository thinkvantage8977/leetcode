
# 思路: 当a>0时,抛物线开口向上,这样给定的数组最大值肯定是在两端, 
# 也就是要么在数组开始,要么在数组的最后, 这样我们可以依次取得最大值.最后的时候翻转一下数组即可.

# 当a<0时, 抛物线开口向下,这样最小值肯定也是在两端, 我们可以依次在两端取最小值.
class Solution(object):

    def fx(self, a, b, c, x):
        return a * x * x + b * x + c

    def sortTransformedArray(self, nums, a, b, c):
        left = 0
        right = len(nums) - 1
        res = []
        while left <= right:
            val1 = self.fx(a, b, c, nums[left])
            val2 = self.fx(a, b, c, nums[right])
            if a > 0:
                if val1 > val2:
                    res.append(val1)
                    left += 1
                else:
                    res.append(val2)
                    right -= 1
            else:
                if val1 < val2:
                    res.append(val1)
                    left += 1
                else:
                    res.append(val2)
                    right -= 1


        return res if a <= 0 else res[::-1]

nums = [-4, -2, 2, 4]
a = 1
b = 3
c = 5

testClass = Solution()
print(testClass.sortTransformedArray(nums, a, b, c))


nums = [-4, -2, 2, 4]
a = -1
b = 3
c = 5
print(testClass.sortTransformedArray(nums, a, b, c))
