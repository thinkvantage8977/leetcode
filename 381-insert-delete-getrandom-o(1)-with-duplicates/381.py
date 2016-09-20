import random

# 思路：用hash记录下标， 删除只需要和末尾元素调换即可


class RandomizedSet(object):

    def __init__(self):
        self.index = {}
        self.l = []

    def insert(self, val):
        if val not in self.index:
            self.l.append(val)
            self.index[val] = [len(self.l) - 1]
        else:
            self.l.append(val)
            self.index[val].append([len(self.l) - 1])

    def remove(self, val):
        if val not in self.index:
            return False
        else:

            i = self.index[val].pop()

            if not self.index[val]:
                del self.index[val]

            if i == len(self.l) - 1:
                self.l.pop()
            else:
                self.l[i] = self.l.pop()
                
                self.index[self.l[i]] = i

            return True

    def getRandom(self):
        i = random.randint(0, len(self.l) - 1)

        return self.l[i]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
