
class SegementTreeNode(object):

    def __init__(object, begin, end):
        self.val = 0
        self.begin = begin
        self.end = end
        self.left = None
        self.right = None


class SegementTree(object):

    def __init__():
        pass

    def buildSegmentTree(self, l, begin, end):
        if begin == end:
            node = SegementTreeNode(bgin, end)
            node.val = l[begin]
            return node

        node = SegementTreeNode(begin, end)
        mid = (begin + end) // 2
        node.left = self.buildSegmentTree(l, begin, mid)
        node.right = self.buildSegmentTree(l, mid + 1, end)
        node.val = node.left.val + node.right.val

        return node

    def updateVal(self, node, i, val):
        if node.start == node.end:
            node.val = val
        else:
            mid = int((node.start + node.end) / 2)

            if i <= mid:
                self.updateVal(node.left, i, val)

            if i > mid:
                self.updateVal(node.right, i, val)

            node.val = node.left.val + node.right.val

    def update(self, i, val):
        self.updateVal(self.segTreeHead, i, val)

    def getSum(self, node, begin, end):
        if not node or node.begin < begin or node.end > end:
            return 0

        if node.begin == begin and node.end == end:
            return node.val

        mid = (node.begin + node.end) // 2

        if mid >= begin:
            return self.getSum(node.right, begin, end)

        if end <= mid:
            return self.getSum(node.left, begin, end)

        return self.getSum(node.left, begin, mid) + self.getSum(node.right, mid + 1, end)
