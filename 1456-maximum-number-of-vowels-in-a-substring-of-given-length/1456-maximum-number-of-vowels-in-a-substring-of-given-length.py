class Solution(object):
    def maxVowels(self, s, k):
        cv=0
        mv=0
        v=["a","e","i","o","u"]
        for i in range(0,k):
            if s[i] in v:
                cv+=1
            mv=max(mv,cv)
            
        for j in range(k,len(s)):
            if s[j-k] in v:
                cv -=1
            if s[j] in v:
                cv +=1
            mv=max(mv,cv)
        return mv


        