class WordDistance(object):

    def __init__(self, words):
        self.d = {}
        for i in range(len(words)):
            if words[i] in self.d:
                self.d[words[i]].append(i)
            else:
                self.d[words[i]] = [i]

    def shortest(self, word1, word2):
        d = float("inf")
        for i in self.d[word1]:
            for j in self.d[word2]:
                d = min(d, abs(i - j))
        return d
