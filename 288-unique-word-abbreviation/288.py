class ValidWordAbbr(object):

    def compress(self, s):
        if len(s) <= 2:
            return s
        else:
            return s[0] + str(len(s) - 2) + s[-1]

    def __init__(self, dictionary):
        self.d = {}
        for i in dictionary:
            c = self.compress(i)
            if c in self.d:
                if i not in self.d[c]:
                    self.d[c].append(i)
            else:
                self.d[c] = [i]

    def isUnique(self, word):
        c = self.compress(word)
        if c not in self.d:
            return True

        if len(self.d[c]) > 1 or self.d[c][0] != word:
            return False
        else:
            return True


# Your ValidWordAbbr object will be instantiated and called as such:

dictionary = ["z", "z", "cake", "card"]
vwa = ValidWordAbbr(dictionary)
print(vwa.isUnique("z"))
print(vwa.isUnique("cart"))
print(vwa.isUnique("cane"))
print(vwa.isUnique("make"))
