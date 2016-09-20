class TreeNode(object):

    def __init__(self, start, end):
        self.val = 0
        self.start = start
        self.end = end
        self.left = None
        self.right = None


class SegementTree(object):

    def buildSegementTree(self, nums, left, right):
        if left == right:
            node = TreeNode(left, right)
            node.val = nums[left]
            return node
        else:
            mid = (left + right) // 2
            node = TreeNode(left, right)
            node.left = self.buildSegementTree(nums, left, mid)
            node.right = self.buildSegementTree(nums, mid + 1, right)
            node.val = node.left.val + node.right.val

            return node

    def __init__(self, nums):
        if nums:
            self.treeRoot = self.buildSegementTree(nums, 0, len(nums) - 1)
        else:
            self.treeRoot = None

    def findRangeSum(self, root, begin, end):
        if not root or root.start > begin or root.end < end:
            return 0

        if root.start == begin and root.end == end:
            return root.val

        mid = (root.start + root.end) // 2
        if end <= mid:
            return self.findRangeSum(root.left, begin, end)
        if begin > mid:
            return self.findRangeSum(root.right, begin, end)

        return self.findRangeSum(root.left, begin, mid) + self.findRangeSum(root.right, mid + 1, end)
