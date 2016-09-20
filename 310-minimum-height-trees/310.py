# Hint: 答案只可能有一个或两个节点。思路为依次删除叶子节点，剩下的1/2个节点即为解。
# 速度问题：如果每次遍历选出叶子节点，速度比较慢，可以每次删除当前叶子节点时，将新的叶子节点记录下来。

class Solution(object):

    def findMinHeightTrees(self, n, edges):
        if n <= 1:
            return [0]
        if not edges:
            return []

        neighbors = [set() for i in range(n)]

        for e in edges:
            neighbors[e[0]].add(e[1])
            neighbors[e[1]].add(e[0])

        leaves = [x for x in range(n) if len(neighbors[x]) == 1]

        while n > 2:
            print(leaves)
            n -= len(leaves)
            newLeaves = []
            for leaf in leaves:
                neighbor = neighbors[leaf].pop()
                neighbors[neighbor].remove(leaf)
                if len(neighbors[neighbor]) == 1:
                    newLeaves.append(neighbor)

            leaves = newLeaves

        return leaves


testClass = Solution()

n = 6
edges = [[0, 3], [1, 3], [2, 3], [4, 3], [5, 4]]

print(testClass.findMinHeightTrees(n, edges))
