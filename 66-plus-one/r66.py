class Solution(object):

    def plusOne(self, digits):
        digits = [0] + digits
        digits[-1] += 1
        for i in range(len(digits) - 1, 0, -1):
            digits[i - 1] += digits[i] // 10
            digits[i] %= 10

        if digits[0] == 0:
            return digits[1:]
        else:
            return digits
