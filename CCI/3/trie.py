import collections

class trieNode(object):

    def __init__(self):
        self.isWord = False
        self.children = collections.defaultdict(trieNode)


class trie(object):

    def __init__(self):
        self.root = trieNode()

    def addWord(self, word):
        node = self.root
        for w in word:
            node = node.children[w]
        node.isWord = True

    def search(self, word, prefix=False):
        node = self.root
        for w in word:
            if w not in node.children:
                return False
            node = node.children[w]

        return node.isWord if prefix == False else True

t = trie()


t.addWord("hello")
t.addWord("world")
t.addWord("my")
t.addWord("name")
t.addWord("is")
t.addWord("weidai")



print(t.search("hello"))
print(t.search("he",True))
print(t.search("hell"))
print(t.search("we",True))


