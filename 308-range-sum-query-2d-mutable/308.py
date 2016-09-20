
class SegementTeee2DNode(object):

    def __init__(self, lr, lc, rr, rc):
        self.leftRow = lr
        self.leftColum = lc
        self.rightRow = rr
        self.rightColum = rc
        self.areaSum = 0
        self.n1 = None
        self.n2 = None
        self.n3 = None
        self.n4 = None


class SegementTree2D(object):

    def __init__(self, matrix):
        if not matrix:
            self.root = None
        else:
            self.root = self.buildSegementTree(0, 0, len(matrix) - 1, len(matrix[0]) - 1, matrix)

    def buildSegementTree(self, lr, lc, rr, rc, matrix):
        if lr > rr or lc > rc:
            return None

        node = SegementTeee2DNode(lr, lc, rr, rc)

        if lr == rr and lc == rc:
            node.areaSum = matrix[lr][lc]
            return node

        rowmid = (lr + rr) // 2
        columnmid = (lc + rc) // 2

        node.n1 = self.buildSegementTree(lr, lc, rowmid, columnmid, matrix)
        node.n2 = self.buildSegementTree(lr, columnmid + 1, rowmid, rc, matrix)
        node.n3 = self.buildSegementTree(rowmid + 1, lc, rr, columnmid, matrix)
        node.n4 = self.buildSegementTree(rowmid + 1, columnmid + 1, rr, rc, matrix)

        node.areaSum += node.n1.areaSum if node.n1 else 0
        node.areaSum += node.n2.areaSum if node.n2 else 0
        node.areaSum += node.n3.areaSum if node.n3 else 0
        node.areaSum += node.n4.areaSum if node.n4 else 0
        return node

    def update(self, r, c, node, val):
        if not node:
            return

        # print("node: ({},{}) - ({},{}) - target ({},{}))".format(node.leftRow, node.leftColum, node.rightRow, node.rightColum, r, c))

        if r > node.rightRow or c > node.rightColum:
            return

        if node.rightRow == node.leftRow and node.leftColum == node.rightColum:
            node.areaSum = val
            return

        rowmid = (node.leftRow + node.rightRow) // 2
        columnmid = (node.leftColum + node.rightColum) // 2
        # print("rowmid ={} colmid = {}".format(rowmid, columnmid))
        if r <= rowmid and c <= columnmid:
            self.update(r, c, node.n1, val)

        if r <= rowmid and c > columnmid:
            self.update(r, c, node.n2, val)

        if r > rowmid and c <= columnmid:
            self.update(r, c, node.n3, val)

        if r > rowmid and c > columnmid:
            self.update(r, c, node.n4, val)

        node.areaSum = 0
        node.areaSum += node.n1.areaSum if node.n1 else 0
        node.areaSum += node.n2.areaSum if node.n2 else 0
        node.areaSum += node.n3.areaSum if node.n3 else 0
        node.areaSum += node.n4.areaSum if node.n4 else 0

    def rangeSum(self, lr, lc, rr, rc, node):
        if not node:
            return 0

        # print("node: ({},{}) - ({},{}) - target ({},{}) - ({},{})".format(node.leftRow, node.leftColum, node.rightRow, node.rightColum, lr, lc, rr, rc))

        if node.leftRow == lr and node.leftColum == lc and node.rightRow == rr and node.rightColum == rc:
            return node.areaSum

        if lr > rr or lc > rc:
            return 0

        if lr > node.rightRow or lc > node.rightColum or rr < node.leftRow or rc < node.leftColum:
            return 0

        rowmid = (node.leftRow + node.rightRow) // 2
        columnmid = (node.leftColum + node.rightColum) // 2

        thisSum = 0
        thisSum += self.rangeSum(lr, lc, min(rr, rowmid), min(rc, columnmid), node.n1)
        thisSum += self.rangeSum(lr, max(lc, columnmid + 1), min(rowmid, rr), rc, node.n2)
        thisSum += self.rangeSum(max(lr, rowmid + 1), lc, rr, min(columnmid, rc), node.n3)
        thisSum += self.rangeSum(max(lr, rowmid + 1), max(lc, columnmid + 1), rr, rc, node.n4)

        return thisSum


class NumMatrix(object):

    def __init__(self, matrix):
        self.segTree = SegementTree2D(matrix)

    def sumRegion(self, row1, col1, row2, col2):
        if self.segTree.root:
            return self.segTree.rangeSum(row1, col1, row2, col2, self.segTree.root)
        else:
            return 0

    def update(self, row, col, val):
        if self.segTree.root:
            self.segTree.update(row, col, self.segTree.root, val)


matrix = [[1, 2]]
testClass = NumMatrix(matrix)


print(testClass.sumRegion(0, 0, 1, 1))
print(testClass.sumRegion(0,1,0,1))
print(testClass.sumRegion(0,0,0,1))

testClass.update(0, 0, 3)
testClass.update(0, 1, 5)
print(testClass.sumRegion(0, 0, 1, 1))


# matrix = [
#     [3, 0, 1, 4, 2],
#     [5, 6, 3, 2, 1],
#     [1, 2, 0, 1, 5],
#     [4, 1, 0, 1, 7],
#     [1, 0, 3, 0, 5]
# ]


# testClass = NumMatrix(matrix)


# print(testClass.sumRegion(2, 1, 4, 3))
# testClass.update(3, 2, 2)
# print(testClass.sumRegion(2, 1, 4, 3))

# print(testClass.sumRegion(2,1,3,4))
