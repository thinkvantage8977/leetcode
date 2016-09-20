class DoubleListNode(object):

    def __init__(self, k, x):
        # record key for bi-directional mapping
        self.key = k
        self.val = x
        self.prev = None
        self.next = None


class LRUCache(object):

    def __init__(self, capacity):
        self.d = {}
        self.head = self.tail = None
        self.size = 0
        self.c = capacity

    def get(self, key):
        if key not in self.d:
            return -1
        node = self.d[key]
        self.moveToTop(node)

    def set(self, key, value):

        if key in self.d:
            self.d[key].val = value
            self.moveToTop(self.d[key])
        else:
            if self.size > self.c:
                del self.d[key]
                if self.head == self.tail:
                    self.head = self.tail = None
                else:
                    self.tail = self.tail.prev
                    self.tail.next = None
                self.size -= 1

            node = DoubleListNode(key, value)
            self.d[key] = node
            self.moveToTop(node)

    def moveToTop(self, node):
        if node is self.head:
            return

        if self.head == None:
            self.head = self.tail = node
        else:

            if node.prev:
                node.prve.next = node.next
                if node.next:
                    node.next.prev = node.prev
                else:
                    self.tail = self.tail.prev
               
                node.next = self.head
                self.head.prev = node
                node.prev = None
                self.head = node
