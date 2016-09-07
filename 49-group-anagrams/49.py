class Solution(object):

    def groupAnagrams(self, strs):
        d = {}
        res = []
        for s in strs:
            l = list(s)
            l.sort()
            news = "".join(l)

            if news in d:
                d[news].append(s)
            else:
                d[news] = [s]

        for value in d.values():
            res.append(value)
        return res
