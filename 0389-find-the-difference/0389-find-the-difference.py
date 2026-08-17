class Solution(object):
    def findTheDifference(self, s, t):
        s = list(s)

        for ch in t:
            if ch in s:
                s[s.index(ch)] = 0
            else:
                return ch