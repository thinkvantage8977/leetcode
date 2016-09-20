class Solution(object):

    def validTree(self, n, edges):
        if len(edges) != n - 1:
            return False

        if n == 0:
            return True

        parents = [0] * n

        for i in range(n):
            parents[i] = i

        for e in edges:
            par1 = parents[e[0]]
            par2 = parents[e[1]]

            while par1 != parents[par1]:
                par1 = parents[par1]

            while par2 != parents[par2]:
                par2 = parents[par2]

            if par1 != par2:
                parents[par2] = par1
                n -= 1

        return n == 1
