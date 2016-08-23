# Definition for a binary tree node.
class TreeNode(object):

    def __init__(self, start, end):
        self.val = 0
        self.start = start
        self.end = end
        self.left = None
        self.right = None


class NumArray(object):
    segTree = []
    n = 0

    def buildSegmentTee(self, root, nums, start, end):
        #print("root = {}, start = {}, end = {}".format(root, start, end))
        if start == end:
            self.segTree[root] = nums[start]
        else:
            mid = int((start + end) / 2)

            self.buildSegmentTee(root * 2 + 1, nums, start, mid)

            self.buildSegmentTee(root * 2 + 2, nums, mid + 1, end)

            self.segTree[root] = self.segTree[
                root * 2 + 1] + self.segTree[root * 2 + 2]

    def __init__(self, nums):
        size = 1
        self.n = len(nums)

        while size < len(nums):
            size *= 2

        size *= 2

        self.segTree = [0 for i in range(0, size - 1)]

        if nums:
            self.buildSegmentTee(0, nums, 0, len(nums) - 1)

        # print(self.segTree)

    def searchForSum(self, root, targetleft, targetright, currentleft, currentright):
        mid = int((currentleft + currentright) / 2)

        if currentleft > targetleft or currentright < targetright:
            return 0

        if currentleft == targetleft and currentright == targetright:
            return self.segTree[root]

        if targetright <= mid:
            return self.searchForSum(root * 2 + 1, targetleft, targetright, currentleft, mid)
        if targetleft > mid:
            return self.searchForSum(root * 2 + 2, targetleft, targetright, mid + 1, currentright)

        return self.searchForSum(root * 2 + 1, targetleft, mid, currentleft, mid) + self.searchForSum(root * 2 + 2, mid + 1, targetright, mid + 1, currentright)

    def sumRange(self, i, j):
        #print(self.segTree)
        return self.searchForSum(0, i, j, 0, self.n - 1)


nums = [-2, 0, 3, -5, 2, -1]


testClass = NumArray([])

print(testClass.sumRange(0, 2))
print(testClass.sumRange(2, 5))
print(testClass.sumRange(0, 5))
