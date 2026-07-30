class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        c=0
        m=0
        for i in range(len(nums)):
            if nums[i]==1:
                c=c+1
                m=max(c,m)
            else:
                c=0
        return m
        