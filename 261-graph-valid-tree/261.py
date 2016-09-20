# 思路：判断一个图是不是一棵树①首先应该有n-1条边　②边没有形成环

# 初始端点n个是独立的, 并且每个端点的父结点为自身索引. 
# 利用并查集, 如果一条边的两个端点的最终父结点不相同, 
# 那么两个端点就可以合并到一个集合中. 最后看是否只有一个集合即可.

class Solution(object):

    def validTree(self, n, edges):

        if n != len(edges) + 1:
            return False

        union = [0] * n
        
        for i in range(n):
            union[i] = i

        print(union)

        for e in edges:
            parent1 = e[0]
            parent2 = e[1]

            while union[parent1] != parent1:
                parent1 = union[parent1]
            while union[parent2] != parent2:
                parent2 = union[parent2]
            print("{} {}".format(parent1, parent2))

            if parent1 != parent2:
                union[parent2] = parent1
                n -= 1

        return n == 1


testClass = Solution()

n = 5
edges = [[0, 1], [0, 2], [0, 3], [1, 4]]

print(testClass.validTree(n, edges))
