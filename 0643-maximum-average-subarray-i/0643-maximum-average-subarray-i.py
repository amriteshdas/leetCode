class Solution(object):
    def findMaxAverage(self, nums, k):
        wavg=sum(nums[:k])
        mavg=wavg

        for i in range(k,len(nums)):
            wavg=wavg-nums[i-k]+nums[i]
            mavg=max(mavg,wavg)
        return float(mavg)/k
        