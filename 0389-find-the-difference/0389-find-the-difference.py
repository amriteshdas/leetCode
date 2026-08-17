class Solution(object):
    def findTheDifference(self, s, t):
        s = list(s)
        for i in range(len(t)):
            if t[i] in s:
                s[s.index(t[i])]=0
            else:
                return t[i]
        