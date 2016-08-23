# Definition for a segement binary tree node.
class TreeNode(object):

    def __init__(self, start, end):
        self.val = 0
        self.start = start
        self.end = end
        self.left = None
        self.right = None


class NumArray(object):
    segTreeHead = None

    def buildSegmentTree(self, nums, left, right):
        if left == right:
            node = TreeNode(left,right)
            node.val = nums[left]
            return node
        else:
            mid = int((left + right) / 2)
            node = TreeNode(left,right)
            node.left = self.buildSegmentTree(nums, left, mid)
            node.right = self.buildSegmentTree(nums, mid + 1, right)
            node.val = node.left.val + node.right.val

            return node

    def __init__(self, nums):
        if nums:
            self.segTreeHead = self.buildSegmentTree(nums, 0, len(nums) - 1)

    def searchForRange(self, root, i, j):
        if not root or root.start > i or root.end < j:
            return 0
        
        if root.start == i and root.end == j:
            return root.val
        
        mid = int((root.start + root.end) / 2)
        if j <= mid:
            return self.searchForRange(root.left, i, j)
        if i > mid:
            return self.searchForRange(root.right, i, j)
        
        return self.searchForRange(root.left, i, mid) + self.searchForRange(root.right, mid + 1, j)

    def sumRange(self, i, j):
        return self.searchForRange(self.segTreeHead, i, j)


nums = [1, 3, 5]

testClass = NumArray(nums)

print(testClass.sumRange(0, 8))
testClass.
# print(testClass.sumRange(2, 5))
# print(testClass.sumRange(0, 5))
