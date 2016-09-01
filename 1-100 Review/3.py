class Solution(object):

    def lengthOfLongestSubstring(self, s):

        # dict stores char c's latest appearing position
        cdict = {}
        ans = head = tail = 0
        while tail < len(s):
            # if found a c that has appeared before, move head to the last
            # position +1 of c of it is after current head
            if s[tail] in cdict:
                head = max(head, cdict[s[tail]] + 1)
                cdict[s[tail]] = tail
            else:
                cdict[s[tail]] = tail

            # so our current str between tail and head always contains no
            # duplicates
            ans = max(ans, tail - head + 1)
            tail += 1
        return ans
