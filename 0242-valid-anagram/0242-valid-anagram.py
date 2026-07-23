class Solution(object):
    def isAnagram(self, s, t):
        cs={}
        ct={}
        for x in s:
            cs[x]=cs.get(x,0)+1
        
        for y in t:
            ct[y]=ct.get(y,0)+1

        if cs==ct:
            return True
        else:
            return False