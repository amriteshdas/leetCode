class Solution(object):
    def toGoatLatin(self, sentence):
        strw = sentence.split()
        v= ["a","e","i","o","u","A","E","I","O","U"]
        ans = []

        count = 0
        p = 1
        for words in strw:

            cw  = words
           
            if cw[0] in v:
                cw= cw + "ma"
                cw = cw + "a"*p
                ans.append(cw)
            else:
                cw = cw[1:]+ cw[0]
                cw = cw + "ma"
                cw = cw + "a"*p
                ans.append(cw)
            p +=1
        return " ".join(ans)


        