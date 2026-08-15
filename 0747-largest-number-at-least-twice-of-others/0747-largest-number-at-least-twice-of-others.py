class Solution(object):
    def dominantIndex(self, nums):
        snums = sorted(set(nums))
        for i in range(len(snums)-1):
            if snums[i]*2 > snums[-1]:
                return -1
        else:
            return nums.index(snums[-1])
        