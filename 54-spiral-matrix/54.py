class Solution(object):

    def spiralOrder(self, matrix):
        ret = []
        while matrix:
            # pop first line
            ret += matrix.pop(0)

            # pop every last element of every left row
            if matrix and matrix[0]:
                for row in matrix:
                    ret.append(row.pop())

            # pop and reverse the last list
            if matrix:
                ret += matrix.pop()[::-1]

            # pop every first element of left row <- reverse order
            if matrix and matrix[0]:
                for row in matrix[::-1]:
                    ret.append(row.pop(0))

        return ret

testClass = Solution()

m = [[1, 2, 3, 4, 5, 6],
     [1, 2, 3, 4, 5, 6],
     [1, 2, 3, 4, 5, 6],
     [1, 2, 3, 4, 5, 6],
     [1, 2, 3, 4, 5, 6]

     ]

print(testClass.spiralOrder(m))
