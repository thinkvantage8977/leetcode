class Vector2D(object):

    def __init__(self, vec2d):
        self.l = []

        for i in vec2d:
            for j in i:
                self.l.append(j)
        self.l = self.l[::-1]

    def next(self):
        return self.l.pop()

    def hasNext(self):
        if self.l:
            return True
        else:
            return False


# Your Vector2D object will be instantiated and called as such:
# i, v = Vector2D(vec2d), []
# while i.hasNext(): v.append(i.next())
