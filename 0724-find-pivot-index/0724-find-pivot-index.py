class Solution(object):
    def pivotIndex(self, nums):
        total = sum(nums)
        l = 0
        for i in range(len(nums)):
            r= total - l -nums[i]
            if r==l:
                return i
            l +=nums[i]
        else:
            return -1


        