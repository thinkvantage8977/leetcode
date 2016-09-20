class Solution(object):

    def verifyPreorder(self, preorder):
        stack = []
        low = -float("inf")

        for p in preorder:
            if p < low:
                return False
            while stack and p > stack[-1]:
                low = stack.pop()
            stack.append(p)

        return True
