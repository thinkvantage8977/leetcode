# Definition for a binary tree node.
class TreeNode(object):

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):

    def constructBST(self, start, end):
        if start >= end:
            return None

        mid = (start + end) // 2

        node = TreeNode(self.nums[mid])

        node.left = self.constructBST(start, mid)
        node.right = self.constructBST(mid + 1, end)

        return node

    def sortedArrayToBST(self, nums):
        if not nums:
            return None
        self.nums = nums
        return self.constructBST(0, len(nums))


testClass = Solution()

nums = [0, 1, 2, 3, 4, 5]

testClass.sortedArrayToBST(nums)
