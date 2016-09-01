class Solution(object):

    def lengthOfLongestSubstring(self, s):
        cdict = {}
        ans = head = tail = 0
        while tail < len(s):
            if s[tail] in cdict:
                head = max(head, cdict[s[tail]] + 1)
                cdict[s[tail]] = tail
            else:
                cdict[s[tail]] = tail
            ans = max(ans, tail - head + 1)
            tail += 1
        return ans
