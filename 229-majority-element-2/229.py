class Solution(object):

    def majorityElement(self, nums):
        if not nums:
            return []

        cadidate1, cadidate2, count1, count2 = 0, 0, 0, 0

        for n in nums:
            if n == cadidate1:
                count1 += 1
            elif n == cadidate2:
                count2 += 1
            elif count1 == 0:
                cadidate1 = n
                count1 = 1
            elif count2 == 0:
                cadidate2 = n
                count2 = 1
            else:
                count1 -= 1
                count2 -= 1

        return [n for n in set([cadidate1, cadidate2]) if nums.count(n) > (len(nums) / 3)]


testClass = Solution()

l = [1, 1, 1, 1, 1, 1,0,0,0,0,0,0,0,0]

print(testClass.majorityElement(l))
