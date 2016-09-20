class TrieNode(object):

    def __init__(self):
        self.isWord = False
        self.children = collections.defaultdict(TrieNode)


class Trie(object):

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for c in word:
            node = node.children[c]
        node.isWord = True

    def search(self, word, isWord=True):
        node = self.root
        for c in word:
            if c not in node.children:
                return False
            node = node.children[c]

        return node.isWord if isWord else True

    def startsWith(self, prefix):
        return self.search(prefix, False)

