class Solution(object):
    def firstMissingPositive(self, nums):
        seen = set(nums)
        for i in range(1,len(nums)+1):
            if i not in seen:
                return i
        else:
                return max(nums)+1
        