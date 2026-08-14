class Solution(object):
    def arrayPairSum(self, nums):
        snum=sorted(nums)
        msum=0
        i = 0
        for _ in range(len(nums)/2):
            msum=msum+min(snum[i],snum[i+1])
            i = i+2
        return msum



        