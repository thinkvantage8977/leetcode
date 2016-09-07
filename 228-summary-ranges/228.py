class Solution(object):

    def summaryRanges(self, nums):
        if not nums:
            return []
        res = []
        head = nums[0]
        previous = nums[0]
        for i in nums:
            if i - previous > 1:
                if head == previous:
                    res.append(str(head))
                else:
                    res.append(str(head) + "->" + str(previous))
                head = i
                previous = i
            else:
                previous = i

        if head == previous:
            res.append(str(head))
        else:
            res.append(str(head) + "->" + str(previous))
        return res


testClass = Solution()

print(testClass.summaryRanges([0, 1, 2, 4, 5, 7]))
