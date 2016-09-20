class Solution(object):

    def dfs(self, current, target):

        #if the target is not in dict return 0 
        if current not in self.relationDict or target not in self.relationDict:
            return 0

        #target == current return 1.0
        if target == current:
            return 1.0

        #relation exists, return valueDict[(current,target)]
        if current in self.relationDict[target]:
            return self.valueDict[(current, target)]
        else:

            #dfs on known relations on current
            for c in self.relationDict[current]:
                if self.marker[c] == 0:
                    self.marker[c] = 1
                    value = self.dfs(c, target)
                    self.marker[c] = 0
                    #got a value, return current value * returned value
                    if value != 0:
                        return value * self.valueDict[(current, c)]
            return 0

    def calcEquation(self, equations, values, queries):
        if not equations or not queries:
            return []


        #store known relations
        self.relationDict = {}

        #store relation matched to values
        self.valueDict = {}

        #marker for dfs
        self.marker = {}

        for i in range(len(equations)):
            e = equations[i]


            #if we know a/b=2.0 then we know b/a=1/2.0
            if e[0] not in self.marker:
                self.marker[e[0]] = 0

            if e[1] not in self.marker:
                self.marker[e[1]] = 0

            if e[0] not in self.relationDict:
                self.relationDict[e[0]] = [e[1]]
            else:
                self.relationDict[e[0]].append(e[1])

            if e[1] not in self.relationDict:
                self.relationDict[e[1]] = [e[0]]
            else:
                self.relationDict[e[1]].append(e[0])

            self.valueDict[(e[0], e[1])] = values[i]
            self.valueDict[(e[1], e[0])] = 1 / values[i]

        res = []

        for q in queries:
            r = self.dfs(q[0], q[1])
            if r == 0:
                res.append(-1.0)
            else:
                res.append(r)

        return res


equations = [["a", "b"], ["b", "c"]]
values = [2.0, 3.0]
queries = [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]]

testClass = Solution()

print(testClass.calcEquation(equations, values, queries))
