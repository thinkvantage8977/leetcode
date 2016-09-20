class IntervalTreeNode(object):

    def __init__(self, Interval):
        self.interval = Interval
        self.maxEnd = Interval.end
        self.left = None
        self.right = None


class Interval(object):

    def __init__(self, start, end):
        self.start = start
        self.end = end


class IntervalTree(object):

    def __init__(self):
        self.root = None

    def insertInterval(self, node, interval):
        if not node:
            return IntervalTreeNode(interval)

        l = node.interval.start

        if interval.start < l:
            node.left = self.insertInterval(node.left)
        else:
            node.right = self.insertInterval(node.right)

        if node.maxEnd < interval.high:
            node.maxEnd = interval.high

        return node

    def searchValue(self, value, node):
        if not node:
            return False

        if value > node.maxEnd:
            return False

        if value < node.interval.end:
            return self.searchValue(node.left, value)
        else:
            return self.searchValue(node.right, value)
