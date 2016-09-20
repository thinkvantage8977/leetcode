
import collections
class TrieNode(object):

    def __init__(object):
        self.children = collections.defaultdict(TrieNode)
        self.isWord = False

class Trie(object):

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for c in word:
            node = node.children[c]
        node.isWord = True

    def search(self, word, prefix=True):
        node = self.root

        for c in word:
            if c not in node.children:
                return False
            node = node.children[c]

        return node.isWord if prefix else True
