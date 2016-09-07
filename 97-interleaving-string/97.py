class Solution(object):

    def isInterleave(self, s1, s2, s3):
        p1 = 0
        p2 = 0
        p3 = 0

        while p3 < len(s3):
            if p1 < len(s1) and s1[p1] == s3[p3]:
                print("s1[p1]={} s3[p3]={} ".format(s1[p1], s3[p3]))

                p1 += 1
                p3 += 1
            elif p2 < len(s2) and s2[p2] == s3[p3]:
                print("s2[p2]={} s3[p3]={} ".format(s2[p2], s3[p3]))

                p2 += 1
                p3 += 1
            else:
                print("p1={} p2={} p3={}".format(p1, p2, p3))
                return False
        return True


testClass = Solution()

print(testClass.isInterleave("aabcc", "dbbca", "aadbbcbcac"))
print(testClass.isInterleave("aabcc", "dbbca", "aadbbbaccc"))
