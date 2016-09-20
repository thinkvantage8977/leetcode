class Solution(object):

    def shortestWordDistance(self, words, word1, word2):
        self.d = {}
        for i in range(len(words)):
            if words[i] in self.d:
                self.d[words[i]].append(i)
            else:
                self.d[words[i]] = [i]

        d = float("inf")
        for i in self.d[word1]:
            for j in self.d[word2]:
                if i != j:
                    d = min(d, abs(i - j))

        return d
