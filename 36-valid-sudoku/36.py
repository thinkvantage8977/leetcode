import collections


class Solution(object):

    def validString(self, s):
        c = collections.Counter(s)
        for key, value in c.items():
            if value > 1 and key != ".":
                return False
        return True

    def isValidSudoku(self, board):
        board = board
        vertical = [""] * 9
        square = [""] * 9

        for i in range(len(board)):
            for j in range(9):
                vertical[i] += board[j][i]

        for i in range(3):
            square[0] += board[i][0] + board[i][1] + board[i][2]
            square[1] += board[i][3] + board[i][4] + board[i][5]
            square[2] += board[i][6] + board[i][7] + board[i][8]
            square[3] += board[i + 3][0] + board[i + 3][1] + board[i + 3][2]
            square[4] += board[i + 3][3] + board[i + 3][4] + board[i + 3][5]
            square[5] += board[i + 3][6] + board[i + 3][7] + board[i + 3][8]
            square[6] += board[i + 6][0] + board[i + 6][1] + board[i + 6][2]
            square[7] += board[i + 6][3] + board[i + 6][4] + board[i + 6][5]
            square[8] += board[i + 6][6] + board[i + 6][7] + board[i + 6][8]

        for i in range(9):
            if (not self.validString(board[i])) or (not self.validString(vertical[i])) or (not self.validString(square[i])):
                return False
        return True

testClass = Solution()

l = [".87654321", "2........", "3........", "4........", "5........", "6........", "7........", "8........", "9........"]

print(testClass.isValidSudoku(l))
