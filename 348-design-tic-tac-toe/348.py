class TicTacToe(object):

    def __init__(self, n):
        self.h1 = [0] * n
        self.h2 = [0] * n
        self.v1 = [0] * n
        self.v2 = [0] * n
        self.leftUpToRightLower1 = [0] * (n * 2)
        self.leftUpToRightLower2 = [0] * (n * 2)
        self.leftLowerToRightUpper1 = [0] * (n * 2)
        self.leftLowerToRightUpper2 = [0] * (n * 2)
        self.n = n

    def move(self, row, col, player):
        if player == 1:
            self.h1[row] += 1
            self.v1[col] += 1
            self.leftLowerToRightUpper1[row - col] += 1
            self.leftUpToRightLower1[row + col] += 1

            if self.h1[row] == self.n or self.v1[col] == self.n or self.leftLowerToRightUpper1[row - col] == self.n or self.leftUpToRightLower1[row + col] == self.n:
                return 1

        if player == 2:
            self.h2[row] += 1
            self.v2[col] += 1
            self.leftLowerToRightUpper2[row - col] += 1
            self.leftUpToRightLower2[row + col] += 1

            if self.h2[row] == self.n or self.v2[col] == self.n or self.leftLowerToRightUpper2[row - col] == self.n or self.leftUpToRightLower2[row + col] == self.n:
                return 2

        return 0


toe = TicTacToe(3)

print(toe.move(0, 0, 1))
print(toe.move(0, 2, 2))
print(toe.move(2, 2, 1))
print(toe.move(1, 1, 2))
print(toe.move(2, 0, 1))
print(toe.move(1, 0, 2))
print(toe.move(2, 1, 1))
