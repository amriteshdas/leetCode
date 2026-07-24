class Solution(object):
    def isIsomorphic(self, s, t):
        mapST = {}
        mapTS = {}

        for i in range(len(s)):

            # Check mapping from s -> t
            if s[i] in mapST:
                if mapST[s[i]] != t[i]:
                    return False
            else:
                mapST[s[i]] = t[i]

            # Check mapping from t -> s
            if t[i] in mapTS:
                if mapTS[t[i]] != s[i]:
                    return False
            else:
                mapTS[t[i]] = s[i]

        return True