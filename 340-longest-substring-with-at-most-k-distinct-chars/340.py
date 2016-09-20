class Solution(object):

    def lengthOfLongestSubstringKDistinct(self, s, k):
        if not s:
            return 0
        if k == 0:
            return 0

        maxlen = -float("inf")

        hashset = {}

        head = 0
        tail = 0

        while tail < len(s):
            if s[tail] in hashset:
                hashset[s[tail]] += 1
                tail += 1
            else:
                while len(hashset) >= k:

                    hashset[s[head]] -= 1
                    if hashset[s[head]] == 0:
                        del hashset[s[head]]
                    head += 1

                hashset[s[tail]] = 1
                tail += 1

            maxlen = max(maxlen, tail - head)

        return maxlen


testClass = Solution()

print(testClass.lengthOfLongestSubstringKDistinct("eceba", 2))
