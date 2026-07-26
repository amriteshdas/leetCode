class Solution(object):
    def isSubsequence(self, s, t):
        p=-1
        l=0
        for ch in s:
            for i in range(len(t)):
                if ch ==t[i] and p<i:
                    p=i
                    l=l+1
                    break

        if l==len(s):
            return True
        else:
            return False
        