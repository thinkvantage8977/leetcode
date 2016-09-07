import collections


class Solution(object):

    def canPermutePalindrome(self, s):
        charDict = collections.Counter(s)

        flag = 0
        for key, values in charDict.items():

            if (values % 2 == 1):
                flag += 1

            if flag > 1:
                return False

        return True

testClass = Solution()


print(testClass.canPermutePalindrome("aab"))
