class Solution(object):
    def minimumPushes(self, word):
        cost=0
        for i in range(1,len(word)+1):
            if i<=8:
                cost +=1
            elif 8<i<=16:
                cost +=2
            elif 16<i<=24:
                cost +=3
            elif 24<i<=26:
                cost = cost+4
            
        return cost
        