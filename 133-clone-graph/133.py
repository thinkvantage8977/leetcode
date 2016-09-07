# Definition for a undirected graph node
# class UndirectedGraphNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []


class Solution(object):

    def DFS(self, node):

        if not node:
            return None

        if node in self.graphDict:
            return self.graphDict[node]

        newNode = UndirectedGraphNode(node.label)
        self.graphDict[node] = newNode

        for i in node.neighbors:
            current = self.DFS(i)
            newNode.neighbors.append(current)
        return newNode

    def cloneGraph(self, node):
        self.graphDict = {}

        node = self.DFS(node)
        return node
