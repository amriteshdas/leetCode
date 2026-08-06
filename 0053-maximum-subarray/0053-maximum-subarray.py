class Solution(object):
    def maxSubArray(self, nums):
        msum= -99999999999999999
        total = 0
        for i in range(len(nums)):
            total =total+nums[i]
            msum = max(total, msum)
            if total<0:
                total = 0
        return msum




        