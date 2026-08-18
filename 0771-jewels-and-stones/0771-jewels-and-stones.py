class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        c = 0
        for i in range(len(stones)):
            if stones[i] in jewels:
                c+=1
        return c
        