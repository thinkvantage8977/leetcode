class ZigzagIterator(object):

    def __init__(self, v1, v2):
        self.v1 = v1
        self.v2 = v2
        self.i = 0

    def next(self):
        if not self.v1:
            return self.v2.pop(0)

        if not self.v2:
            return self.v1.pop(0)

        if self.i == 0:
            self.i = 1
            return self.v1.pop(0)

        if self.i == 1:
            self.i = 0
            return self.v2.pop(0)

    def hasNext(self):
        if self.v1 or self.v2:
            return True
        else:
            return False


# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())
