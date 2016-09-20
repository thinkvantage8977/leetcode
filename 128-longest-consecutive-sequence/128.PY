class Solution(object):

    def longestConsecutive(self, nums):
        if not nums:
            return 0

        s = set(nums)

        maxL = 0

        for i in nums:
            if i in s:
                c = 1
                up = i + 1
                down = i - 1
                while up in s:
                    c += 1
                    s.remove(up)
                    up += 1

                while down in s:
                    c += 1
                    s.remove(down)
                    down -= 1
                maxL = max(maxL, c)
                
        return maxL


testClass = Solution()

print(testClass.longestConsecutive([100, 4, 200, 1, 3, 2]))
