import queue


class Stack(object):

    def __init__(self):
        self.q1 = queue.Queue()
        self.q2 = queue.Queue()

    def push(self, x):

        while not self.q1.empty():
            self.q2.put(self.q1.get())
        self.q1.put(x)

        while not self.q2.empty():
            self.q1.put(self.q2.get())

    def pop(self):
        return self.q1.get()

    def top(self):
        t = self.q1.get()
        self.push(t)
        return t

    def empty(self):
        return self.q1.empty()
