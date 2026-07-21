class Solution(object):
    def missingNumber(self, nums):
        c = 0
        for _ in range(len(nums)):

            if c in nums:
                c =c+1
            else:
                return c
        return c