import collections


class triesNode(object):

    def __init__(self):
        self.isWord = False
        self.children = collections.defaultdict(triesNode)


class WordDictionary(object):

    def __init__(self):
        self.root = triesNode()

    def addWord(self, word):
        node = self.root
        for c in word:
            node = node.children[c]
        node.isWord = True

    def search(self, word):
        return self.searchWord(word, self.root)

    def searchWord(self, word, current):
        if len(word) == 1:
            if word in current.children and current.children[word].isWord:
                return True
            if word == "." and current.children:
                for c in current.children.values():
                    if c.isWord:
                        return True
                return False
            return False
        else:
            node = current
            res = False
            if word[0] == ".":
                for value in node.children.values():
                    res = res or self.searchWord(word[1:], value)
                return res
            else:
                if word[0] not in node.children:
                    return False
                else:
                    res = self.searchWord(word[1:], node.children[word[0]])
            return res


wordDictionary = WordDictionary()
wordDictionary.addWord("bad")
wordDictionary.addWord("dad")
wordDictionary.addWord("mad")
print(wordDictionary.search("pad"))
print(wordDictionary.search("bad"))
print(wordDictionary.search(".ad"))
print(wordDictionary.search("b.."))
