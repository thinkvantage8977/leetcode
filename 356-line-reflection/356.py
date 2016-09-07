class Solution(object):

    def isReflected(self, points):
        if not points:
            return True

        maxX = max([i[0] for i in points])
        minX = min([i[0] for i in points])

        mid = (maxX + minX) /  float(2)

        d = {}
        print(mid)

        for i in points:
            if (mid - i[0]) not in d:
                d[mid - i[0]] = [i[1]]
            else:
                d[mid - i[0]].append(i[1])

        print(d)
        for i in points:
            if (i[0] - mid) not in d:
                
                return False
            elif i[1] not in d[i[0] - mid]:
                return False
        return True


testClass = Solution()

l = [[0,0],[1,0]]

print(testClass.isReflected(l))
