class TrieNode(object):
    def __init__(self):
        self.is_word = False
        self.children = collections.defaultdict(TrieNode)

class Trie(object):
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for c in word:
            node = node.children[c]
        node.is_word = True

    def search(self, word, is_word=True):
        node = self.root
        for c in word:
            if c not in node.children:
                return False
            node = node.children[c]
        return node.is_word if is_word else True

    def startsWith(self, prefix):
        return self.search(prefix, False)