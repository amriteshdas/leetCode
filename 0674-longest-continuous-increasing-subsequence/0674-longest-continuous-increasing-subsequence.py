class Solution(object):
    def findLengthOfLCIS(self, nums):
        c=1
        mc=0
        for i in range(1,len(nums)):
            if nums[i]>nums[i-1]:
                c +=1
            else:
                c=1
            mc = max(mc,c)
        if len(nums)<2:
            return 1
        else:
            return mc
                

        