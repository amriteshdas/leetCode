class Solution(object):
    def plusOne(self, digits):
        ans=[]
        num="".join(map(str, digits))
        numi = int(num)+1
        nums=str(numi)
        for x in nums:
            ans.append(int(x))
        return(ans)

        