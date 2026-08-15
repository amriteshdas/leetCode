class Solution(object):
    def findNumbers(self, nums):
        c=0
        for i in range(len(nums)):
            if len(str(nums[i]))&1==0:
                c+=1
        return c

        