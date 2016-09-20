class DoubleListNode(object):
    def __init__(self, k, x):
        # record key for bi-directional mapping
        self.key = k
        self.val = x
        self.prev = None
        self.next = None

class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.cache = {}
        self.head = self.tail = None
        self.cap = capacity

    def get(self, key):
        if key not in self.cache:
            return -1
        self.moveToTop(self.cache[key])
        return self.cache[key].val

    def set(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: nothing
        """
        if key in self.cache:
            self.cache[key].val = value
            self.moveToTop(self.cache[key])
        else:
            if len(self.cache) == self.cap:
                del self.cache[self.tail.key]
                # remove only node
                if self.head == self.tail:
                    self.head = self.tail = None
                else:
                    self.tail = self.tail.prev
                    self.tail.next = None
            node = DoubleListNode(key, value)
            self.cache[key] = node
            self.moveToTop(node)
        
    def moveToTop(self, node):
        """
        :type node: DoubleListNode
        rtypr: nothing
        """
        if node is self.head:
            return
        # add first node
        if self.head is None:
            self.head = self.tail = node
        else:
            # node in cache
            if node.prev:
                node.prev.next = node.next
                if node.next:
                    node.next.prev = node.prev
                else:
                    self.tail = self.tail.prev
            
            # node in cache or new node
            node.prev, node.next = None, self.head
            self.head.prev = node
            self.head = node