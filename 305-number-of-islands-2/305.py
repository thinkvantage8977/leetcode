
# 思路: 一道并查集的题目, 并无什么陷阱. 
# 主要思路还是为每一个位置初始化一个父结点, 
# 因为是一个二维数组, 比较方便的方式是二维转化为一维. 
# 也就是每一个位置的父结点设置(x*n+y), 其中(x, y)为其位置坐标. 
# 然后每次插入一个新元素的时候查上下左右地图是不是有相邻的陆地,
#  当然在此之前还需要建立一张二维的地图用来维护地图的状态. 
#  这样如果新添加的一个点的时候默认小岛数量增加1, 
#  但是如果这个新添加的陆地有相邻的陆地, 就将其合并成一块陆地, 
#  并且小岛数量-1. 因为他有上下左右四个方向, 所以有可能当前点连接了之前并不相连的小岛, 
#  在当前结点碰到第一个相邻的陆地的时候, 他被并入了那块陆地, 
#  如果之后他碰到了另一个小岛和他属于不同的小岛, 则还要合并两个小岛, 又会让小岛数量-1. 

class Solution(object):

    def traceToFather(self, par):
        if self.parents[par] != par:
            self.parents[par] = self.traceToFather(self.parents[self.parents[par]])
            return self.parents[par]
        else:
            return par

    def numIslands2(self, m, n, positions):
        self.parents = [0] * (m * n)

        for i in range(m * n):
            self.parents[i] = i
        # print(self.parents)
        islandmap = [[0 for j in range(n)] for i in range(m)]

        res = []
        islands = 0

        for p in positions:
            par1 = n * p[0] + p[1]
            neighbors = []

            # if neighbor is within the map and has an i on it, we need to merge it
            if p[0] + 1 < m and islandmap[p[0] + 1][p[1]] == 1:
                neighbors.append(n * (p[0] + 1) + p[1])
            if p[0] - 1 >= 0 and islandmap[p[0] - 1][p[1]] == 1:
                neighbors.append(n * (p[0] - 1) + p[1])
            if p[1] + 1 < n and islandmap[p[0]][p[1] + 1] == 1:
                neighbors.append(n * (p[0]) + p[1] + 1)
            if p[1] - 1 >= 0 and islandmap[p[0]][p[1] - 1] == 1:
                neighbors.append(n * (p[0]) + p[1] - 1)

            for neighbor in neighbors:
                par1 = n * p[0] + p[1]
                par2 = neighbor

                # trace to its root
                par1 = self.traceToFather(par1)

                par2 = self.traceToFather(par2)

                #if two 1 1 points belongs to different root, they were two islands, merge them
                if par1 != par2:
                    self.parents[par2] = par1
                    islands -= 1

                print(self.parents)
            islands += 1
            islandmap[p[0]][p[1]] = 1
            res.append(islands)

        return res


testClass = Solution()

m = 3
n = 3
p = [[0, 0], [0, 1], [0, 2], [1, 0],  [2, 1], [2, 2], [1, 2]]

print(testClass.numIslands2(m, n, p))
