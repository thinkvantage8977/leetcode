class Solution(object):

    def computeArea(self, A, B, C, D, E, F, G, H):
        if A >= G or C <= E or B >= H or D <= F:
            overlap = 0
        else:
            if A <= E:
                width = min(G - E, C - E)
            else:
                width = min(C - A, G - A)

            if D <= H:
                height = min(D - B, D - F)
            else:
                height = min(H - F, H - B)
            overlap = width * height
        return (C - A) * (D - B) + (G - E) * (H - F) - overlap
