class Solution(object):
    def isIsomorphic(self, s, t):
        mapst={}
        mapts={}


        if len(s)!=len(t):
            return False

        else:

            for i in range (len(s)):
                if s[i] in mapst:
                    if mapst[s[i]] != t[i]:
                        return False
                else:
                    mapst[s[i]] = t[i]

                if t[i] in mapts:
                    if mapts[t[i]] != s[i]:
                        return False
                else:
                    mapts[t[i]] = s[i]
            return True




        